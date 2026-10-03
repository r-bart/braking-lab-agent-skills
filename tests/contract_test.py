"""Regression guards for references the domain-only verifier previously omitted."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from verify_contract import verify_ray_contract  # noqa: E402


class RayContractTest(unittest.TestCase):
    def setUp(self):
        self.domain = json.loads((ROOT / "tests/contract/tool-catalog.json").read_text())
        self.ray = json.loads((ROOT / "tests/contract/ray-tools.json").read_text())
        self.skills = {
            path.parent.name: path.read_text(encoding="utf-8")
            for path in (ROOT / "skills").glob("*/SKILL.md")
        }

    def tool(self, name):
        return next(tool for tool in self.ray["tools"] if tool["name"] == name)

    def check(self):
        return verify_ray_contract(self.ray, self.domain, self.skills)

    def test_current_skill_routes_are_known(self):
        self.assertEqual(self.check(), 7)

    def test_unknown_underscore_tool_is_rejected(self):
        self.skills["setup-library"] += "\nOpen `ray_openSetupFille`."
        with self.assertRaisesRegex(AssertionError, "Unknown Ray tools"):
            self.check()

    def test_missing_domain_mirror_is_rejected(self):
        self.ray["tools"] = [t for t in self.ray["tools"] if t["name"] != "ray_recordSetupComparison"]
        with self.assertRaisesRegex(AssertionError, "Missing domain mirrors"):
            self.check()

    def test_source_mismatch_is_rejected(self):
        self.ray["sourceRevision"] = "0" * 40
        with self.assertRaisesRegex(AssertionError, "source mismatch"):
            self.check()

    def test_catalog_mismatch_is_rejected(self):
        self.ray["version"] = "101-0000000000000000"
        with self.assertRaisesRegex(AssertionError, "catalog mismatch"):
            self.check()

    def test_duplicate_tools_are_rejected(self):
        self.ray["tools"].append(deepcopy(self.tool("ray_openSetupFile")))
        with self.assertRaisesRegex(AssertionError, "Duplicate typed tools"):
            self.check()

    def test_file_opener_cannot_become_a_write(self):
        self.tool("ray_openSetupFile")["readOnlyHint"] = False
        with self.assertRaisesRegex(AssertionError, "read-only"):
            self.check()

    def test_import_cannot_become_a_read(self):
        self.tool("ray_importSetupFile")["readOnlyHint"] = True
        with self.assertRaisesRegex(AssertionError, "separate write"):
            self.check()

    def test_sensitive_mutation_cannot_become_a_read(self):
        self.tool("ray_recordSetupComparison")["readOnlyHint"] = True
        with self.assertRaisesRegex(AssertionError, "Sensitive mutation"):
            self.check()

    def test_file_entrypoint_cannot_omit_the_file(self):
        self.tool("ray_openSetupFile")["required"] = []
        with self.assertRaisesRegex(AssertionError, "entrypoint contract"):
            self.check()

    def test_sensitive_tools_cannot_disappear_from_model_discovery(self):
        original = deepcopy(self.ray)
        for name in ("commitSetupAssociation", "retireSetupAssociation", "recordSetupComparison"):
            with self.subTest(name=name):
                self.ray = deepcopy(original)
                self.tool(f"ray_{name}")["visibility"] = ["app"]
                with self.assertRaisesRegex(AssertionError, "discoverable"):
                    self.check()


if __name__ == "__main__":
    unittest.main()

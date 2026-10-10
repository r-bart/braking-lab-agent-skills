"""Publication checks must distinguish a prepared ZIP from a review-ready release."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from verify_submission import validate, no_private_bindings, package_file  # noqa: E402


class SubmissionTest(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.openai = self.manifest["extensions"]["com.openai"]

    def test_missing_demo_blocks_review_ready(self):
        self.openai["review"].pop("demo_recording_url", None)
        self.assertEqual(validate(self.manifest), ["Real reviewer-accessible demo recording URL"])
        with self.assertRaisesRegex(ValueError, "demo recording"):
            validate(self.manifest, ready=True)

    def test_review_ready_requires_https_demo(self):
        self.openai["review"]["demo_recording_url"] = "http://example.com/demo"
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            validate(self.manifest, ready=True)
        self.openai["review"]["demo_recording_url"] = "https://example.com/demo"
        self.assertEqual(validate(self.manifest, ready=True), [])

    def test_subtitle_limit_is_submission_limit(self):
        self.openai["interface"]["shortDescription"] = "x" * 31
        with self.assertRaisesRegex(ValueError, "30 characters"):
            validate(self.manifest)

    def test_support_page_required_not_derived_from_homepage(self):
        del self.openai["interface"]["supportURL"]
        with self.assertRaisesRegex(ValueError, "supportURL"):
            validate(self.manifest)

    def test_urls_cannot_embed_credentials(self):
        self.openai["interface"]["websiteURL"] = "https://user:pass@example.com/"
        with self.assertRaisesRegex(ValueError, "without credentials"):
            validate(self.manifest)

    def test_exact_review_counts_and_known_tools(self):
        original = deepcopy(self.openai["review"]["test_cases"])
        self.openai["review"]["test_cases"]["positive"].pop()
        with self.assertRaisesRegex(ValueError, "Exactly 5"):
            validate(self.manifest)
        self.openai["review"]["test_cases"] = original
        original["negative"].pop()
        with self.assertRaisesRegex(ValueError, "Exactly 3"):
            validate(self.manifest)
        original["negative"].append({"description": "Unsupported", "prompt": "Unsupported"})
        original["positive"][0]["tools_triggered"] = "ray_invented"
        with self.assertRaisesRegex(ValueError, "unknown tool"):
            validate(self.manifest)

    def test_private_bindings_hooks_and_access_rejected_recursively(self):
        for value in [{"apps": []}, {"hooks": {}}, {"test_credentials": {}}, {"reviewer_instructions": "private"}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                no_private_bindings({"compatibility": [value]})

    def test_paths_cannot_escape_package(self):
        for path in ["../plugin.json", "./../plugin.json", "/etc/passwd", "./assets\\logo.png"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                package_file(ROOT, path)

    def test_invalid_image_and_onboarding_rejected(self):
        self.openai["interface"]["logo"] = "./plugin.json"
        with self.assertRaisesRegex(ValueError, "PNG"):
            validate(self.manifest)
        self.openai["interface"]["logo"] = "./assets/braking-lab-v5.png"
        self.openai["onboardingSkill"] = "./skills/missing/SKILL.md"
        with self.assertRaisesRegex(ValueError, "Missing packaged"):
            validate(self.manifest)

    def test_worldwide_and_translation_limits(self):
        self.openai["publication"]["countries"] = ["ES"]
        with self.assertRaisesRegex(ValueError, "all available"):
            validate(self.manifest)
        self.openai["publication"]["countries"] = []
        self.openai["publication"]["translations"]["es-ES"]["subtitle"] = "x" * 31
        with self.assertRaisesRegex(ValueError, "30 characters"):
            validate(self.manifest)

    def test_starter_prompts_are_unique_single_line(self):
        self.openai["interface"]["defaultPrompt"] = ["Prompt", "Prompt"]
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validate(self.manifest)
        self.openai["interface"]["defaultPrompt"] = ["Prompt\nMore"]
        with self.assertRaisesRegex(ValueError, "single-line"):
            validate(self.manifest)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Check that every MCP function named by a skill exists in the pinned catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "tests" / "contract" / "tool-catalog.json"
RAY_CATALOG = ROOT / "tests" / "contract" / "ray-tools.json"
RAY_NAME = re.compile(r"\bray_[A-Za-z][A-Za-z0-9_]*\b")
FUNCTION_NAME = re.compile(
    r"(?:get|read|import|list|compare|save|create|update|delete|link|unlink|search|"
    r"generate|preview|commit|retire|confirm|record|add|remix|build|"
    r"report|explain)[A-Z][A-Za-z0-9]*$"
)
BACKTICK_NAME = re.compile(r"`([A-Za-z][A-Za-z0-9]*)`")
DIRECT_CALL = re.compile(r"\bbrakinglab\.([A-Za-z][A-Za-z0-9]*)\s*\(")


def verify_ray_contract(snapshot: dict, domain: dict, skills: dict[str, str]) -> int:
    assert snapshot["sourceRevision"] == domain["sourceRevision"], "Ray/domain source mismatch"
    assert snapshot["version"] == domain["version"], "Ray/domain catalog mismatch"
    tools = snapshot["tools"]
    known = {tool["name"]: tool for tool in tools}
    assert len(known) == len(tools), "Duplicate typed tools"
    assert {f"ray_{name}" for name in domain["names"]} <= known.keys(), "Missing domain mirrors"
    for tool in tools:
        assert isinstance(tool["readOnlyHint"], bool), "Unknown read-only policy"
        assert set(tool["required"]) <= set(tool["inputFields"]), "Invalid required fields"
        assert set(tool["visibility"]) <= {"app", "model"}, "Unknown tool visibility"
    unknown = {
        skill: sorted(set(RAY_NAME.findall(content)) - known.keys())
        for skill, content in skills.items()
        if set(RAY_NAME.findall(content)) - known.keys()
    }
    assert not unknown, f"Unknown Ray tools: {unknown}"
    opener = known["ray_openSetupFile"]
    assert opener["readOnlyHint"] is True, "File opener must remain read-only"
    assert opener["required"] == ["file"], "File entrypoint contract changed"
    assert known["ray_importSetupFile"]["readOnlyHint"] is False, "Import is a separate write"
    for name in ("commitSetupAssociation", "retireSetupAssociation", "recordSetupComparison"):
        tool = known[f"ray_{name}"]
        assert tool["readOnlyHint"] is False, "Sensitive mutation cannot become read-only"
        assert "model" in tool["visibility"], "Direct confirmation tool must be discoverable"
    return len(set().union(*(set(RAY_NAME.findall(content)) for content in skills.values())))


def main() -> None:
    snapshot = json.loads(CATALOG.read_text(encoding="utf-8"))
    names = snapshot["names"]
    assert len(names) == len(set(names)), "Duplicate MCP functions in snapshot"
    assert snapshot["version"].split("-", 1)[0] == str(len(names))
    assert re.fullmatch(r"[0-9a-f]{40}", snapshot["sourceRevision"])

    known = set(names)
    references: dict[str, set[str]] = {}
    skills: dict[str, str] = {}
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        content = skill.read_text(encoding="utf-8")
        skills[skill.parent.name] = content
        tokens = set(BACKTICK_NAME.findall(content)) | set(DIRECT_CALL.findall(content))
        referenced = {
            name for name in tokens if FUNCTION_NAME.fullmatch(name) or name == "whoami"
        }
        assert referenced, f"No MCP function named in {skill}"
        references[skill.parent.name] = referenced

    unknown = {
        skill: sorted(found - known)
        for skill, found in references.items()
        if found - known
    }
    assert not unknown, f"Unknown MCP functions: {unknown}"
    count = len(set.union(*references.values()))
    print(f"Catalog {snapshot['version']}: {count} referenced functions verified")
    ray = json.loads(RAY_CATALOG.read_text(encoding="utf-8"))
    ray_count = verify_ray_contract(ray, snapshot, skills)
    print(f"Ray tools: {ray_count} referenced tools verified against {len(ray['tools'])} definitions")


if __name__ == "__main__":
    main()

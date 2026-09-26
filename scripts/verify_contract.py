#!/usr/bin/env python3
"""Check that every MCP function named by a skill exists in the pinned catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "tests" / "contract" / "tool-catalog.json"
FUNCTION_NAME = re.compile(
    r"(?:get|list|compare|save|create|update|delete|link|unlink|search|"
    r"generate|preview|commit|retire|confirm|record|add|remix|build|"
    r"report|explain)[A-Z][A-Za-z0-9]*$"
)
BACKTICK_NAME = re.compile(r"`([A-Za-z][A-Za-z0-9]*)`")
DIRECT_CALL = re.compile(r"\bbrakinglab\.([A-Za-z][A-Za-z0-9]*)\s*\(")


def main() -> None:
    snapshot = json.loads(CATALOG.read_text(encoding="utf-8"))
    names = snapshot["names"]
    assert len(names) == len(set(names)), "Duplicate MCP functions in snapshot"
    assert snapshot["version"].split("-", 1)[0] == str(len(names))
    assert re.fullmatch(r"[0-9a-f]{40}", snapshot["sourceRevision"])

    known = set(names)
    references: dict[str, set[str]] = {}
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        content = skill.read_text(encoding="utf-8")
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


if __name__ == "__main__":
    main()

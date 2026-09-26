#!/usr/bin/env python3
"""Verify the provider packages share one identity, MCP, and skill source."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "tests" / "schemas"
EXPECTED_SKILLS = {
    "calendar-events",
    "debrief",
    "lap-comparison",
    "race-engineer",
    "race-week",
    "setup-coaching",
    "setup-evaluation",
    "setup-library",
    "track-notes",
}
PRODUCTION_MCP = "https://mcp.brakinglab.com/mcp"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_json(path: Path, schema_path: Path) -> dict:
    data = read_json(path)
    schema = read_json(schema_path)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(data)
    return data


def main() -> None:
    portable = validate_json(ROOT / "plugin.json", SCHEMAS / "plugin.schema.json")
    mcp = validate_json(ROOT / "mcp.json", SCHEMAS / "mcp.schema.json")
    claude = read_json(ROOT / ".claude-plugin" / "plugin.json")
    claude_mcp = read_json(ROOT / ".mcp.json")
    openai_app = read_json(ROOT / "openai" / "app.json")
    marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")
    codex_marketplace = read_json(ROOT / ".agents" / "plugins" / "marketplace.json")

    assert portable["name"] == claude["name"] == "braking-lab-race-engineer"
    assert portable["version"] == claude["version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+", portable["version"])
    assert len(mcp["mcpServers"]) == len(claude_mcp["mcpServers"]) == 1
    assert mcp["mcpServers"]["braking-lab"] == {
        "type": "streamable-http",
        "url": PRODUCTION_MCP,
    }
    assert claude_mcp["mcpServers"]["braking-lab"] == {
        "type": "http",
        "url": PRODUCTION_MCP,
    }
    assert marketplace["plugins"][0]["name"] == portable["name"]
    assert marketplace["plugins"][0]["source"] == {
        "source": "github",
        "repo": "r-bart/braking-lab-agent-skills",
    }
    assert codex_marketplace["name"] == "braking-lab"
    assert len(codex_marketplace["plugins"]) == 1
    assert codex_marketplace["plugins"][0]["name"] == portable["name"]
    assert codex_marketplace["plugins"][0]["source"] == {
        "source": "local",
        "path": "./",
    }
    assert "apps" not in portable["extensions"]["com.openai"]
    assert re.fullmatch(
        r"asdk_app_[A-Za-z0-9_-]+", openai_app["apps"]["braking-lab"]["id"]
    )
    assert openai_app["apps"]["braking-lab"]["required"] is True
    interface = portable["extensions"]["com.openai"]["interface"]
    for asset_key in ("composerIcon", "logo"):
        asset_path = interface[asset_key]
        assert asset_path.startswith("./assets/")
        assert (ROOT / asset_path).is_file()

    skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    assert skill_dirs == EXPECTED_SKILLS, f"Unexpected skill set: {skill_dirs ^ EXPECTED_SKILLS}"
    for name in sorted(skill_dirs):
        directory = ROOT / "skills" / name
        assert not directory.is_symlink(), f"Skill must be a real directory: {name}"
        assert (directory / "SKILL.md").is_file(), f"Missing SKILL.md: {name}"
        subprocess.run(["agentskills", "validate", str(directory)], check=True)

    print("Package verified: 9 skills, 2 provider manifests, one production MCP URL")


if __name__ == "__main__":
    main()

"""Run the public installer against a scratch project and mocked agent CLI."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "dist/braking-lab-portable-0.2.0.zip"
INSTALLER = ROOT / "install.sh"


def run(cwd: Path, *extra: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "sh",
            str(INSTALLER),
            "--agent",
            "codex",
            "--scope",
            "project",
            "--archive",
            str(ARCHIVE),
            "--yes",
            *extra,
        ],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> None:
    assert ARCHIVE.is_file(), "Run scripts/build_archive.py first"
    with tempfile.TemporaryDirectory() as directory:
        cwd = Path(directory)
        result = run(cwd, "--skills", "all", "--no-mcp")
        assert result.returncode == 0, result.stderr
        skill_root = cwd / ".agents/skills"
        assert len(list(skill_root.glob("*/SKILL.md"))) == 9

        result = run(cwd, "--skills", "debrief", "--no-mcp")
        assert result.returncode == 0, result.stderr
        assert (skill_root / "debrief/.braking-lab-installed").is_file()
        assert (next(skill_root.glob(".braking-lab-backup-*/debrief/SKILL.md"))).is_file()

        other = skill_root / "calendar-events"
        (other / ".braking-lab-installed").unlink()
        result = run(cwd, "--skills", "calendar-events", "--no-mcp")
        assert result.returncode != 0 and "leaving it untouched" in result.stderr
        assert (other / "SKILL.md").is_file()

        result = run(cwd, "--skills", "debrief,debrief", "--no-mcp")
        assert result.returncode != 0 and "Duplicate skill" in result.stderr

    with tempfile.TemporaryDirectory() as directory:
        cwd = Path(directory)
        binary = cwd / "bin"
        binary.mkdir()
        trace = cwd / "codex-commands.txt"
        mock = binary / "codex"
        mock.write_text(
            "#!/bin/sh\nprintf '%s\\n' \"$*\" >> \"$CODEX_MOCK_TRACE\"\n"
            "if [ \"$1 $2\" = 'mcp get' ]; then exit 1; fi\n",
            encoding="utf-8",
        )
        mock.chmod(0o755)
        env = {**os.environ, "PATH": f"{binary}:{os.environ['PATH']}", "CODEX_MOCK_TRACE": str(trace)}
        result = run(cwd, "--skills", "race-engineer", env=env)
        assert result.returncode == 0, result.stderr
        assert trace.read_text(encoding="utf-8").splitlines() == [
            "mcp get braking-lab",
            "mcp add braking-lab --url https://mcp.brakinglab.com/mcp",
        ]
    print("Installer smoke passed: nine skills, managed update, collision, duplicate, Codex MCP")


if __name__ == "__main__":
    main()

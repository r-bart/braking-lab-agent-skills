#!/usr/bin/env python3
"""Build public provider archives from one canonical skills directory."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from shutil import copyfile
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
VERSION = MANIFEST["version"]
OUTPUT_DIR = ROOT / "dist"
SKILL_FILES = sorted(path for path in (ROOT / "skills").glob("**/*") if path.is_file())


def add_file(archive: ZipFile, path: Path, name: str | None = None) -> None:
    if path.is_symlink():
        raise ValueError(f"Symlink in package: {path}")
    archive.write(path, name or str(path.relative_to(ROOT)))


def build(flavor: str) -> Path:
    output = OUTPUT_DIR / f"braking-lab-{flavor}-{VERSION}.zip"
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        add_file(archive, ROOT / "assets" / "icon.png")
        for path in SKILL_FILES:
            add_file(archive, path)

        if flavor == "claude":
            add_file(archive, ROOT / ".claude-plugin" / "plugin.json")
            add_file(archive, ROOT / ".mcp.json")
        elif flavor == "portable":
            add_file(archive, ROOT / "plugin.json")
            add_file(archive, ROOT / "mcp.json")
        else:
            raise ValueError(f"Unknown package flavor: {flavor}")

    with ZipFile(output) as archive:
        names = set(archive.namelist())
        assert len(names) == len(archive.namelist()), "Duplicate archive entries"
        assert sum(name in names for name in ("mcp.json", ".mcp.json")) == 1
        assert len([name for name in names if name.endswith("/SKILL.md")]) == 9
    print(f"Built {output}")
    return output


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    archives = [build(flavor) for flavor in ("claude", "portable")]
    installer = OUTPUT_DIR / f"braking-lab-install-{VERSION}.sh"
    copyfile(ROOT / "install.sh", installer)
    installer.chmod(0o755)
    checksums = "".join(
        f"{sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
        for path in [*archives, installer]
    )
    (OUTPUT_DIR / "SHA256SUMS").write_text(checksums, encoding="utf-8")


if __name__ == "__main__":
    main()

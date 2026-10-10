#!/usr/bin/env python3
"""Build public provider archives from one canonical skills directory."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from shutil import copyfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from verify_submission import validate as verify_submission, no_private_bindings


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
VERSION = MANIFEST["version"]
OUTPUT_DIR = ROOT / "dist"
SKILL_FILES = sorted(path for path in (ROOT / "skills").glob("**/*") if path.is_file())


def add_file(archive: ZipFile, path: Path, name: str | None = None) -> None:
    if not path.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError("Package input escapes root")
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("Symlink in package")
    info = ZipInfo(name or path.relative_to(ROOT).as_posix(), (2000, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, path.read_bytes())


def build(flavor: str) -> Path:
    if flavor not in {"claude", "portable"}:
        raise ValueError("Unknown package flavor")
    verify_submission(MANIFEST, ROOT)
    output = OUTPUT_DIR / f"braking-lab-{flavor}-{VERSION}.zip"
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        interface = MANIFEST["extensions"]["com.openai"]["interface"]
        for asset_path in sorted({interface[key] for key in ("logo", "composerIcon")}):
            add_file(archive, ROOT / asset_path)
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
        assert ".app.json" not in names
        assert not any(name.startswith("hooks/") for name in names)
        for name in names:
            if name.endswith(".json"):
                no_private_bindings(json.loads(archive.read(name)))
        assert sum(name in names for name in ("mcp.json", ".mcp.json")) == 1
        assert len([name for name in names if name.endswith("/SKILL.md")]) == 10
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

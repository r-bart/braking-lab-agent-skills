#!/usr/bin/env python3
"""Validate public OpenAI metadata; --ready also requires the real demo URL.

This does not certify OAuth, reviewer access, policy acceptance or live UI rendering.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import struct
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_MCP = "https://mcp.brakinglab.com/mcp"
URL_KEYS = ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: object, limit: int, field: str, single_line: bool = False) -> None:
    require(isinstance(value, str) and bool(value.strip()), f"Missing {field}")
    require(len(value) <= limit, f"{field} exceeds {limit} characters")
    require(not re.search(r"[\x00-\x08\x0b-\x1f\x7f]", value), f"Unsupported controls in {field}")
    if single_line:
        require("\n" not in value and "\r" not in value, f"{field} must be single-line")


def https(value: object, field: str) -> None:
    text(value, 1024, field, True)
    parsed = urlsplit(value)
    require(parsed.scheme == "https" and bool(parsed.hostname) and parsed.username is None and parsed.password is None,
            f"{field} must be HTTPS without credentials")


def package_file(root: Path, value: object) -> Path:
    require(isinstance(value, str) and value.startswith("./"), "Asset/skill paths must start with ./")
    path = PurePosixPath(value)
    require(not path.is_absolute() and ".." not in path.parts and "\\" not in value, "Unsafe package path")
    target = root / path
    require(target.is_file(), "Missing packaged asset/skill")
    current = root
    for part in path.parts:
        current = current / part
        require(not current.is_symlink(), "Symlinked package asset/skill")
    require(target.resolve().is_relative_to(root.resolve()), "Asset/skill escapes package")
    return target


def no_private_bindings(value: object) -> None:
    if isinstance(value, dict):
        require(value.get("apps") is None, "Public ZIP must not contain apps bindings")
        require("hooks" not in value, "Public ZIP must not contain lifecycle hooks")
        require(not {"test_credentials", "reviewer_instructions"} & value.keys(), "Reviewer access belongs in the secure portal")
        for child in value.values():
            no_private_bindings(child)
    elif isinstance(value, list):
        for child in value:
            no_private_bindings(child)


def validate(manifest: dict, root: Path = ROOT, ready: bool = False) -> list[str]:
    no_private_bindings(manifest)
    o = manifest["extensions"]["com.openai"]
    i = o["interface"]
    for key, limit in [("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80), ("category", 120)]:
        text(i.get(key), limit, key, key != "longDescription")
    for key in URL_KEYS:
        https(i.get(key), key)
    prompts = i.get("defaultPrompt", [])
    prompts = [prompts] if isinstance(prompts, str) else prompts
    require(isinstance(prompts, list) and len(prompts) <= 3, "At most three starter prompts")
    for prompt in prompts:
        text(prompt, 128, "defaultPrompt", True)
        require("@" not in prompt, "Starter prompts must omit app mentions")
    require(len(prompts) == len(set(prompts)), "Duplicate starter prompt")
    for key, minimum in [("logo", 256), ("composerIcon", 48)]:
        asset = package_file(root, i.get(key))
        data = asset.read_bytes()
        require(len(data) <= 5 * 1024 * 1024 and data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24,
                "Public icons must be PNG, at most 5 MiB")
        width, height = struct.unpack(">II", data[16:24])
        require(minimum <= width <= 4096 and width == height, f"{key} must be square, {minimum}–4096 px")
    onboarding = o.get("onboardingSkill")
    if onboarding is not None:
        require(onboarding.startswith("./skills/") and onboarding.endswith("/SKILL.md"), "Invalid onboarding skill")
        package_file(root, onboarding)
    mcp = json.loads((root / "mcp.json").read_text(encoding="utf-8"))
    require(mcp["mcpServers"] == {"braking-lab": {"type": "streamable-http", "url": PRODUCTION_MCP}}, "Use exactly the reviewed production MCP")
    no_private_bindings(mcp)
    review = o["review"]
    require(isinstance(review.get("commerce"), bool), "Commerce must be declared")
    text(review.get("commerce_description"), 4000, "commerce_description")
    domain = json.loads((root / "tests/contract/tool-catalog.json").read_text())["names"]
    ray = [item["name"] for item in json.loads((root / "tests/contract/ray-tools.json").read_text())["tools"]]
    known = set(domain + ray + ["execute_code"])
    for polarity, count in [("positive", 5), ("negative", 3)]:
        cases = review["test_cases"][polarity]
        require(isinstance(cases, list) and len(cases) == count, f"Exactly {count} {polarity} cases required")
        for case in cases:
            for key in ["description", "prompt"] + (["tools_triggered", "expected_behavior"] if polarity == "positive" else []):
                text(case.get(key), 4000, f"{polarity}.{key}")
            if polarity == "positive":
                tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", case["tools_triggered"])
                require(all(token in known for token in tokens), "Review case names an unknown tool/function")
            for key in ("expected_output_url",):
                if key in case:
                    https(case[key], key)
            for url in case.get("file_attachment_urls", []):
                https(url, "file_attachment_urls")
    pending = []
    demo = review.get("demo_recording_url")
    if demo:
        https(demo, "demo_recording_url")
    else:
        pending.append("Real reviewer-accessible demo recording URL")
    publication = o["publication"]
    require(publication.get("countries") == [], "User requested all available countries")
    text(publication.get("release_notes"), 4000, "release_notes")
    for locale, translation in publication.get("translations", {}).items():
        text(locale, 30, "locale", True)
        require(bool(translation), "Empty translation")
        if translation.get("subtitle") is not None:
            text(translation["subtitle"], 30, "translated subtitle", True)
        if translation.get("description") is not None:
            text(translation["description"], 4000, "translated description")
    if ready:
        require(not pending, "; ".join(pending))
    return pending


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ready", action="store_true")
    parser.add_argument("--check-urls", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    pending = validate(manifest, ready=args.ready)
    if args.check_urls:
        interface = manifest["extensions"]["com.openai"]["interface"]
        evidence = {"websiteURL": "Braking Lab", "supportURL": "support@brakinglab.com", "privacyPolicyURL": "Privacy Policy", "termsOfServiceURL": "Terms of Service"}
        for key in URL_KEYS:
            request = Request(interface[key], headers={"User-Agent": "BrakingLab-Publication-Check/1.0"})
            with urlopen(request, timeout=20) as response:
                https(response.url, f"{key} redirect")
                content = response.read(2 * 1024 * 1024).decode("utf-8")
                require(response.status == 200 and evidence[key] in content, f"Unverified public {key}")
            print(f"Public {key}: verified")
    print("Public package metadata verified. Live review journeys remain a separate gate.")
    for item in pending:
        print(f"Pending: {item}")


if __name__ == "__main__":
    main()

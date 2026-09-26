#!/usr/bin/env python3
"""Opt-in, read-only Codex routing probe for the bilingual skill corpus."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests" / "cases" / "skill-routing.json"
SKILL_PATH = re.compile(r"braking-lab-race-engineer/[^/]+/skills/([^/]+)/SKILL\.md")


def cases() -> list[dict[str, str]]:
    corpus = json.loads(CASES.read_text(encoding="utf-8"))
    result = []
    for skill, kinds in corpus.items():
        for kind in ("direct", "indirect", "negative"):
            entry = kinds[kind]
            expected = entry.get("expected", skill)
            for lang in ("es", "en"):
                result.append(
                    {
                        "id": f"{skill}-{kind}-{lang}",
                        "skill": skill,
                        "kind": kind,
                        "lang": lang,
                        "expected": expected,
                        "prompt": entry[lang],
                    }
                )
    assert len(result) == 54
    return result


def run_case(case: dict[str, str], timeout: int) -> dict:
    # The test asks the model to choose and load a skill while explicitly
    # forbidding MCP calls. Live account behavior is tested separately.
    constraint = (
        "\n\nRouting test only: load the relevant installed Braking Lab skill "
        "and identify it. Do not call MCP, access account data, or change anything."
    )
    process = subprocess.run(
        [
            "codex", "exec", "--ephemeral", "-s", "read-only",
            "-c", "approval_policy=never", "--json",
            "-C", str(ROOT), case["prompt"] + constraint,
        ],
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    loaded = []
    for line in process.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item") or {}
        if event.get("type") == "item.completed":
            command = item.get("command") or ""
            for skill in SKILL_PATH.findall(command):
                if skill not in loaded:
                    loaded.append(skill)
    return {
        **case,
        "loaded": loaded,
        "passed": process.returncode == 0 and bool(loaded) and loaded[0] == case["expected"],
        "exitCode": process.returncode,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=54)
    parser.add_argument("--lang", choices=("es", "en"))
    parser.add_argument("--kind", choices=("direct", "indirect", "negative"))
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()
    selected = [
        case for case in cases()
        if (not args.lang or case["lang"] == args.lang)
        and (not args.kind or case["kind"] == args.kind)
    ][: args.limit]
    results = []
    for case in selected:
        try:
            result = run_case(case, args.timeout)
        except subprocess.TimeoutExpired:
            result = {**case, "loaded": [], "passed": False, "exitCode": None}
        results.append(result)
        print(f"{case['id']}: {'PASS' if result['passed'] else 'FAIL'} {result['loaded']}", flush=True)
    output = ROOT / "dist" / "routing-results.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sum(r['passed'] for r in results)}/{len(results)} passed; {output}")


if __name__ == "__main__":
    main()

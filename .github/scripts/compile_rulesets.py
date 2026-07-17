#!/usr/bin/env python3
"""Compile repository rule sources into mihomo MRS and sing-box SRS files."""

from __future__ import annotations

import argparse
import filecmp
import ipaddress
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


MRS_DOMAIN_DIR = Path("Clash/domainset")
MRS_IP_DIR = Path("Clash/ip")
SRS_DIRS = (
    Path("sing-box/domainset"),
    Path("sing-box/non_ip"),
    Path("sing-box/ip"),
)


def github_warning(root: Path, source: Path, message: str) -> None:
    relative = source.relative_to(root).as_posix()
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::warning file={relative}::{message}", flush=True)
    else:
        print(f"WARNING {relative}: {message}", flush=True)


def source_lines(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8-sig", errors="strict").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def normalize_ip_rules(lines: list[str]) -> tuple[list[str], set[str]]:
    networks: list[str] = []
    unsupported: set[str] = set()

    for line in lines:
        parts = [part.strip() for part in line.split(",")]
        if len(parts) == 1:
            rule_type = "RAW"
            value = parts[0]
        else:
            rule_type = parts[0].upper()
            if rule_type == "DOMAIN":
                # Upstream uses a harmless sentinel domain to keep empty
                # classical rule sets non-empty. It is not an IP rule.
                continue
            if rule_type not in {"IP-CIDR", "IP-CIDR6"} or len(parts) < 2:
                unsupported.add(rule_type)
                continue
            value = parts[1]

        try:
            network = ipaddress.ip_network(value, strict=False)
        except ValueError:
            unsupported.add(rule_type)
            continue

        if rule_type == "IP-CIDR" and network.version != 4:
            unsupported.add(rule_type)
            continue
        if rule_type == "IP-CIDR6" and network.version != 6:
            unsupported.add(rule_type)
            continue
        networks.append(str(network))

    return networks, unsupported


def run_compiler(command: list[str], output: Path) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, check=True)
    if not output.is_file() or output.stat().st_size == 0:
        raise RuntimeError(f"compiler produced an empty output: {output}")


def stage_mrs(
    root: Path, stage: Path, mihomo: Path
) -> dict[Path, Path]:
    staged: dict[Path, Path] = {}

    for source in sorted((root / MRS_DOMAIN_DIR).glob("*.txt")):
        if not source_lines(source):
            github_warning(root, source, "empty domain rule set; MRS output skipped")
            continue

        target = source.with_suffix(".mrs")
        staged_output = stage / target.relative_to(root)
        staged_output.parent.mkdir(parents=True, exist_ok=True)
        run_compiler(
            [
                str(mihomo),
                "convert-ruleset",
                "domain",
                "text",
                str(source),
                str(staged_output),
            ],
            staged_output,
        )
        staged[target] = staged_output

    normalized_dir = stage / "_normalized_ip"
    for source in sorted((root / MRS_IP_DIR).glob("*.txt")):
        networks, unsupported = normalize_ip_rules(source_lines(source))
        if unsupported:
            rule_types = ", ".join(sorted(unsupported))
            github_warning(
                root,
                source,
                f"contains MRS-incompatible rule types ({rule_types}); output skipped",
            )
            continue
        if not networks:
            github_warning(root, source, "contains no IP CIDR rules; MRS output skipped")
            continue

        normalized = normalized_dir / source.name
        normalized.parent.mkdir(parents=True, exist_ok=True)
        normalized.write_text("\n".join(networks) + "\n", encoding="utf-8")

        target = source.with_suffix(".mrs")
        staged_output = stage / target.relative_to(root)
        staged_output.parent.mkdir(parents=True, exist_ok=True)
        run_compiler(
            [
                str(mihomo),
                "convert-ruleset",
                "ipcidr",
                "text",
                str(normalized),
                str(staged_output),
            ],
            staged_output,
        )
        staged[target] = staged_output

    return staged


def stage_srs(
    root: Path, stage: Path, sing_box: Path
) -> dict[Path, Path]:
    staged: dict[Path, Path] = {}

    for relative_dir in SRS_DIRS:
        for source in sorted((root / relative_dir).glob("*.json")):
            target = source.with_suffix(".srs")
            staged_output = stage / target.relative_to(root)
            staged_output.parent.mkdir(parents=True, exist_ok=True)
            run_compiler(
                [
                    str(sing_box),
                    "rule-set",
                    "compile",
                    "--output",
                    str(staged_output),
                    str(source),
                ],
                staged_output,
            )
            staged[target] = staged_output

    return staged


def reconcile(
    managed_dirs: tuple[Path, ...],
    extension: str,
    staged: dict[Path, Path],
) -> tuple[int, int]:
    changed = 0
    removed = 0
    expected = set(staged)

    for directory in managed_dirs:
        for existing in directory.glob(f"*{extension}"):
            if existing not in expected:
                existing.unlink()
                removed += 1

    for target, staged_output in staged.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.is_file() and filecmp.cmp(target, staged_output, shallow=False):
            continue
        shutil.copyfile(staged_output, target)
        changed += 1

    return changed, removed


def append_summary(
    mrs_total: int,
    srs_total: int,
    changed: int,
    removed: int,
) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with Path(summary_path).open("a", encoding="utf-8") as summary:
        summary.write(
            "## Binary rule-set compilation\n\n"
            f"- MRS outputs: {mrs_total}\n"
            f"- SRS outputs: {srs_total}\n"
            f"- Changed outputs: {changed}\n"
            f"- Removed stale outputs: {removed}\n"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--mihomo", type=Path, required=True)
    parser.add_argument("--sing-box", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    mihomo = args.mihomo.resolve()
    sing_box = args.sing_box.resolve()

    if not mihomo.is_file():
        raise FileNotFoundError(mihomo)
    if not sing_box.is_file():
        raise FileNotFoundError(sing_box)

    with tempfile.TemporaryDirectory(prefix="ruleset-build-") as temporary:
        stage = Path(temporary)
        mrs = stage_mrs(root, stage, mihomo)
        srs = stage_srs(root, stage, sing_box)

        mrs_changed, mrs_removed = reconcile(
            (root / MRS_DOMAIN_DIR, root / MRS_IP_DIR),
            ".mrs",
            mrs,
        )
        srs_changed, srs_removed = reconcile(
            tuple(root / directory for directory in SRS_DIRS),
            ".srs",
            srs,
        )

    changed = mrs_changed + srs_changed
    removed = mrs_removed + srs_removed
    print(
        f"Compiled {len(mrs)} MRS and {len(srs)} SRS files; "
        f"{changed} changed, {removed} stale files removed.",
        flush=True,
    )
    append_summary(len(mrs), len(srs), changed, removed)


if __name__ == "__main__":
    main()

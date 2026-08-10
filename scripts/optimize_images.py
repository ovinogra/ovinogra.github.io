#!/usr/bin/env python3

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

from PIL import Image
from PIL import PngImagePlugin


METADATA_COMMENT = "Made my Moonrise"
SUPPORTED_SUFFIXES = {".png"}


def optimize_png(path: Path) -> bool:
    with Image.open(path) as image:
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("Comment", METADATA_COMMENT)
        image.save(path, format="PNG", optimize=True, pnginfo=pnginfo)
    return True


def optimize_image(path: Path) -> bool:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return optimize_png(path)
    return False


def expand_inputs(inputs: list[str]) -> list[Path]:
    results: list[Path] = []
    seen: set[Path] = set()

    for value in inputs:
        has_glob = any(char in value for char in "*?[]")
        candidates: list[Path] = []

        if has_glob:
            candidates = [Path(match) for match in glob.glob(value, recursive=True)]
        else:
            path = Path(value)
            if path.is_dir():
                candidates = list(path.rglob("*"))
            else:
                candidates = [path]

        for candidate in candidates:
            if not candidate.is_file():
                continue
            if candidate.suffix.lower() not in SUPPORTED_SUFFIXES:
                continue
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            results.append(candidate)

    return results


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Optimize PNG images with Pillow and inject Moonrise metadata."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Image files, directories, or glob patterns (e.g. assets/img/**).",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    files = expand_inputs(args.paths)

    if not files:
        print("No supported image files found.")
        return 0

    optimized_count = 0
    skipped_count = 0

    for path in files:
        changed = optimize_image(path)
        status = "optimized" if changed else "skipped"
        print(f"{status}: {path}")
        if changed:
            optimized_count += 1
        else:
            skipped_count += 1

    print(f"Done. Optimized {optimized_count} file(s), skipped {skipped_count} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

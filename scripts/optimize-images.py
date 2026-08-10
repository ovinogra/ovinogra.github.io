#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image


JPEG_QUALITY = 88


def optimize_png(path: Path) -> None:
    with Image.open(path) as image:
        image.save(path, format="PNG", optimize=True)


def optimize_jpeg(path: Path) -> None:
    with Image.open(path) as image:
        optimized = image.convert("RGB") if image.mode not in {"RGB", "L"} else image
        optimized.save(
            path,
            format="JPEG",
            optimize=True,
            quality=JPEG_QUALITY,
            progressive=True,
        )


def optimize_image(path: Path) -> bool:
    suffix = path.suffix.lower()

    if suffix == ".png":
        optimize_png(path)
        return True

    if suffix in {".jpg", ".jpeg"}:
        optimize_jpeg(path)
        return True

    return False


def restage(path: Path) -> None:
    subprocess.run(["git", "add", str(path)], check=True)


def main(argv: list[str]) -> int:
    for name in argv:
        path = Path(name)
        if not path.is_file():
            continue

        if optimize_image(path):
            restage(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

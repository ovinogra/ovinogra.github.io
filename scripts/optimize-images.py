#!/usr/bin/env python3

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image
from PIL import PngImagePlugin


METADATA_COMMENT = "Moonrise"


def optimize_png(path: Path) -> bool:
    with Image.open(path) as image:
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("Comment", METADATA_COMMENT)
        image.save(path, format="PNG", optimize=True, pnginfo=pnginfo)

    return True


def optimize_jpeg(path: Path) -> bool:
    with Image.open(path) as image:
        optimized = image.convert("RGB") if image.mode not in {"RGB", "L"} else image.copy()

    original_size = path.stat().st_size

    with tempfile.NamedTemporaryFile(suffix=path.suffix, dir=path.parent, delete=False) as temporary_file:
        temporary_path = Path(temporary_file.name)

    try:
        optimized.save(
            temporary_path,
            format="JPEG",
            optimize=True,
            quality=88,
            progressive=True,
            comment=METADATA_COMMENT.encode("utf-8"),
        )

        optimized_size = temporary_path.stat().st_size
        if optimized_size >= original_size:
            temporary_path.unlink(missing_ok=True)
            return False

        os.replace(temporary_path, path)
        return True
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


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
        print(f"Optimizing: {name}")
        path = Path(name)
        if not path.is_file():
            continue

        if optimize_image(path):
            restage(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

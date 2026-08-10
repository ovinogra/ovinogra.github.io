#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

import click
from PIL import Image


METADATA_COMMENT = "Made my Moonrise"
RAW_DIR = Path("assets/img/illustrations_raw")
OUTPUT_DIR = Path("assets/img/illustrations")
SUPPORTED_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}
JPEG_QUALITY = 88


def _to_rgb(image: Image.Image) -> Image.Image:
    if image.mode in {"RGBA", "LA"}:
        background = Image.new("RGB", image.size, (255, 255, 255))
        alpha = image.getchannel("A")
        background.paste(image.convert("RGB"), mask=alpha)
        return background
    if image.mode == "P":
        return image.convert("RGB")
    if image.mode not in {"RGB", "L"}:
        return image.convert("RGB")
    if image.mode == "L":
        return image.convert("RGB")
    return image.copy()


def export_as_jpeg(input_path: Path, output_path: Path, quality: int) -> bool:
    with Image.open(input_path) as image:
        prepared = _to_rgb(image)
        prepared.save(
            output_path,
            format="JPEG",
            optimize=True,
            progressive=True,
            quality=quality,
            comment=METADATA_COMMENT.encode("utf-8"),
        )
    return True


def collect_raw_images(raw_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in raw_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    )


def run(input_dir: Path, output_dir: Path, quality: int) -> int:

    if not input_dir.exists() or not input_dir.is_dir():
        raise click.ClickException(f"Input directory not found: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    files = collect_raw_images(input_dir)

    if not files:
        click.echo(f"No supported source images found in {input_dir}.")
        return 0

    exported_count = 0

    for source_path in files:
        target_path = output_dir / f"{source_path.stem}.jpeg"
        export_as_jpeg(source_path, target_path, quality)
        exported_count += 1
        click.echo(f"exported: {source_path} -> {target_path}")

    click.echo(f"Done. Exported {exported_count} JPEG file(s).")
    return 0


@click.option(
    "--input-dir",
    type=click.Path(path_type=Path, file_okay=False, dir_okay=True),
    default=RAW_DIR,
    show_default=True,
    help="Input directory of source artwork.",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path, file_okay=False, dir_okay=True),
    default=OUTPUT_DIR,
    show_default=True,
    help="Output directory for optimized JPEGs.",
)
@click.option(
    "--quality",
    type=click.IntRange(1, 100),
    default=JPEG_QUALITY,
    show_default=True,
    help="JPEG quality.",
)
def main(input_dir: Path, output_dir: Path, quality: int) -> None:
    raise SystemExit(run(input_dir, output_dir, quality))


if __name__ == "__main__":
    main()

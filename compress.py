#!/usr/bin/env python3
"""
compress.py — Image & GIF compressor
--------------------------------------
Compresses PNG, JPG, JPEG, WEBP, and GIF files in a folder.
NEVER increases file size — if compression makes a file larger,
the original is copied as-is.

Usage:
    python compress.py                        # compresses current folder
    python compress.py path/to/folder         # compresses specific folder
    python compress.py path/to/folder -q 70   # custom quality (1–95, default 75)
    python compress.py path/to/folder -o out  # custom output folder
"""

import sys
import argparse
import shutil
import tempfile
from pathlib import Path
from PIL import Image, ImageSequence

GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RED    = "\033[91m"
DIM    = "\033[2m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def fmt_size(b):
    if b < 1024:        return f"{b} B"
    if b < 1024 ** 2:   return f"{b / 1024:.1f} KB"
    return f"{b / 1024 ** 2:.2f} MB"


def try_compress_gif(src: Path, quality: int) -> bytes:
    img = Image.open(src)
    frames, durations = [], []

    for frame in ImageSequence.Iterator(img):
        fr = frame.convert("RGBA")
        colors = max(32, int(256 * (quality / 95)))
        fr = fr.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
        frames.append(fr)
        durations.append(frame.info.get("duration", 100))

    if not frames:
        return src.read_bytes()

    with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    frames[0].save(
        tmp_path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        loop=img.info.get("loop", 0),
        duration=durations,
    )
    data = tmp_path.read_bytes()
    tmp_path.unlink()
    return data


def try_compress_image(src: Path, quality: int) -> bytes:
    img = Image.open(src)
    ext = src.suffix.lower()

    with tempfile.NamedTemporaryFile(suffix=src.suffix, delete=False) as tmp:
        tmp_path = Path(tmp.name)

    if ext == ".png":
        img = img.convert("RGBA") if img.mode in ("RGBA", "P") else img.convert("RGB")
        img.save(tmp_path, format="PNG", optimize=True, compress_level=9)

    elif ext in (".jpg", ".jpeg"):
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(tmp_path, format="JPEG", quality=quality, optimize=True, progressive=True, subsampling=2)

    elif ext == ".webp":
        img.save(tmp_path, format="WEBP", quality=quality, method=6)

    else:
        img.save(tmp_path, optimize=True, quality=quality)

    data = tmp_path.read_bytes()
    tmp_path.unlink()
    return data


def compress_folder(folder: Path, output: Path, quality: int):
    files = sorted(f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in SUPPORTED)

    if not files:
        print(f"{YELLOW}  No supported images found in {folder}{RESET}")
        return

    output.mkdir(parents=True, exist_ok=True)

    total_orig = 0
    total_final = 0
    skipped = 0

    print(f"\n{BOLD}{CYAN}  Compressing {len(files)} file(s)  →  {output}{RESET}\n")
    print(f"  {'File':<38} {'Original':>10} {'Output':>10} {'Saved':>9}  Note")
    print(f"  {DIM}{'─' * 78}{RESET}")

    for src in files:
        dst = output / src.name
        orig_size = src.stat().st_size

        try:
            if src.suffix.lower() == ".gif":
                compressed = try_compress_gif(src, quality)
            else:
                compressed = try_compress_image(src, quality)

            if len(compressed) < orig_size:
                dst.write_bytes(compressed)
                final_size = len(compressed)
                saving_pct = (orig_size - final_size) / orig_size * 100
                color = GREEN if saving_pct > 10 else YELLOW
                note = ""
            else:
                shutil.copy2(src, dst)
                final_size = orig_size
                saving_pct = 0.0
                color = DIM
                note = f"{DIM}already optimal{RESET}"
                skipped += 1

            total_orig  += orig_size
            total_final += final_size

            if saving_pct > 0:
                pct_str = f"{color}▼{saving_pct:5.1f}%{RESET}"
            else:
                pct_str = f"{DIM}     —{RESET}"

            print(f"  {src.name:<38} {fmt_size(orig_size):>10} {fmt_size(final_size):>10}  {pct_str}  {note}")

        except Exception as e:
            print(f"  {RED}✗ {src.name:<36} {e}{RESET}")
            shutil.copy2(src, dst)
            total_orig  += orig_size
            total_final += orig_size

    total_saved = total_orig - total_final
    total_pct   = (total_saved / total_orig * 100) if total_orig else 0

    print(f"\n  {DIM}{'─' * 78}{RESET}")
    print(f"  {BOLD}Total{RESET}   {fmt_size(total_orig):>48}  {fmt_size(total_final):>10}  "
          f"{GREEN}▼{total_pct:.1f}% saved{RESET}")
    if skipped:
        print(f"  {DIM}{skipped} file(s) were already optimal — originals kept unchanged.{RESET}")
    print(f"\n  {GREEN}✓ Done!{RESET}  Output → {BOLD}{output}{RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Compress images and GIFs. Never increases file size.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("folder", nargs="?", default=".",
                        help="Folder to compress (default: current folder)")
    parser.add_argument("-o", "--output", default=None,
                        help="Output folder (default: <folder>/compressed)")
    parser.add_argument("-q", "--quality", type=int, default=75,
                        help="Quality for JPG/WEBP/GIF, 1–95 (default: 75)")
    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        print(f"{RED}Error: '{folder}' is not a valid folder.{RESET}")
        sys.exit(1)

    quality = max(1, min(95, args.quality))
    output  = Path(args.output).resolve() if args.output else folder / "compressed"

    compress_folder(folder, output, quality)


if __name__ == "__main__":
    main()
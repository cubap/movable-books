"""Generate web-friendly JPEG derivatives from MNHS flap-experiment TIFFs.

Creates:
  - viewable previews (long edge 1400, q 82) into .preview/ for inspection
  - site derivatives (long edge 1600, q 85) into assets/images/<demo>/
"""
from pathlib import Path

from PIL import Image

SRC_ROOT = Path(r"B:\Repositories\movable-books\fixtures\MNHS_Flap_Experiments")
OUT_ROOT = Path(__file__).resolve().parent.parent
PREVIEW_DIR = OUT_ROOT / ".preview"
WEB_DIRS = {
    "Cloth Book": OUT_ROOT / "assets" / "images" / "mnhs-cloth-book",
    "Scrapbook": OUT_ROOT / "assets" / "images" / "mnhs-scrapbook",
}

PREVIEW_EDGE = 1400
WEB_EDGE = 1600
WEB_QUALITY = 85


def convert(src: Path, dst: Path, long_edge: int, quality: int) -> None:
    img = Image.open(src)
    img = img.convert("RGB")
    w, h = img.size
    scale = long_edge / max(w, h)
    if scale < 1:
        img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    print(f"{src.name} -> {dst.relative_to(OUT_ROOT)} {img.size}")


def main() -> None:
    for set_name, out_dir in WEB_DIRS.items():
        for src in sorted((SRC_ROOT / set_name).glob("*.tif")):
            stem = src.stem.replace("flap_experiment_", "")
            preview = PREVIEW_DIR / f"{set_name.replace(' ', '-')}-{stem}-preview.jpg"
            web = out_dir / f"{stem}.jpg"
            convert(src, preview, PREVIEW_EDGE, 82)
            convert(src, web, WEB_EDGE, WEB_QUALITY)


if __name__ == "__main__":
    main()

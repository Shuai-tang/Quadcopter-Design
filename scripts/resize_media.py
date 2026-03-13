#!/usr/bin/env python3
"""将 media/ 目录下的照片缩小，最大宽度 1200px，JPEG 质量 85%。"""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("请先安装: pip install Pillow")
    raise

MEDIA_DIR = Path(__file__).resolve().parent.parent / "media"
MAX_WIDTH = 1200
JPEG_QUALITY = 85


def resize_image(path: Path) -> None:
    img = Image.open(path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    w, h = img.size
    if w <= MAX_WIDTH:
        # 仅压缩质量
        img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        return
    ratio = MAX_WIDTH / w
    new_size = (MAX_WIDTH, int(h * ratio))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
    print(f"  已缩小: {path.name}")


def main():
    if not MEDIA_DIR.is_dir():
        print(f"目录不存在: {MEDIA_DIR}")
        return
    for path in MEDIA_DIR.iterdir():
        if path.suffix.lower() in (".jpg", ".jpeg", ".png"):
            print(f"处理: {path.name}")
            resize_image(path)
    print("完成。")


if __name__ == "__main__":
    main()

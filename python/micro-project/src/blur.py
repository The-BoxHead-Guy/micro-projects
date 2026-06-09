from pathlib import Path
from PIL import Image, ImageFilter

assets = Path(__file__).resolve().parent.parent / "assets"

print(assets)

before = Image.open(assets / "landscape.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save(assets / "blurred.bmp")

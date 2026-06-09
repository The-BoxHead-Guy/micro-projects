from pathlib import Path
from PIL import Image, ImageFilter

assets = Path(__file__).resolve().parent.parent / "assets"

before = Image.open(assets / "landscape.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save(assets / "edged.bmp")

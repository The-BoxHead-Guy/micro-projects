from PIL import Image, ImageFilter

from paths import ASSETS

before = Image.open(ASSETS / "landscape.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save(ASSETS / "edged.bmp")

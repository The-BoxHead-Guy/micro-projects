from PIL import Image, ImageFilter

from paths import ASSETS

before = Image.open(ASSETS / "landscape.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save(ASSETS / "blurred.bmp")

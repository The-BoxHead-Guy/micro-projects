import qrcode

img = qrcode.make("https://rutaweb.net/jhonleon")

type(img)

img.save("jhonleon.png", "PNG")  # pyright: ignore[reportArgumentType]

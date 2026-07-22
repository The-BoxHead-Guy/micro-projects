import qrcode

img = qrcode.make("https://rutaweb.net/jhonleon")

print(type(img))

img.save("jhonleon.png", "PNG")

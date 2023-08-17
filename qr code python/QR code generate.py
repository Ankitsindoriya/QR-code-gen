import qrcode as qr
img = qr.make("https://github.com/Ankitsindoriya")
img.save("my github profile.png")
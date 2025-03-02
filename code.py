import qrcode

data = "https://github.com"
qr = qrcode.make(data)
qr.save("qrcode.png")

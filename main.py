import qrcode

input_data = "https://www.linkedin.com/in/cansel-islamo%C4%9Flu/"
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)

import qrcode 

data = 'Don\'t forget to subscribe'

qr = qrcode.QRCode(version = 1, box_size=10, border =5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image
img.save('C:/Users/user/Documents/Python beginner projects/qrcode.png')

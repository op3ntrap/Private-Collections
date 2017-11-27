import qrcode
qr = qrcode.QRCode(
    version=30 ,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
print(img)
img.save('qrcode.png')
from IPython.display import Image
![title](qrcode.png "ShowMyImage")

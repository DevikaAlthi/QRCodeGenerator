import qrcode
from PIL import Image

# Correcting the class name to QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5
)

# Adding the data to the QR code
qr.add_data("https://mail.google.com/mail/u/0/#all")
qr.make(fit=True)

# Creating an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Saving the image to a file
img.save("devika_replit.png")

print("QR code generated and saved as devika_replit.png")

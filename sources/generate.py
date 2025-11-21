import qrcode
from PIL import Image
import os

def generate_qr(link, name_qr):

    if not os.path.exists('./static/images'):
        os.mkdir('./static/images')

    file_path = f'./static/images/{name_qr}.png'

    qr = qrcode.QRCode()
    qr.add_data(link)

    img = qr.make_image()
    img.save(file_path)


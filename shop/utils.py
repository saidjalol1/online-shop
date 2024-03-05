import os
import random
import string
from barcode import Code128
from barcode.writer import ImageWriter
from django.conf import settings


def generate_barcode_data(length=10):
    # Generate barcode data
    barcode_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return barcode_data


def generate_barcode_image(barcode_data, order_id):
    # Generate barcode image
    code128 = Code128(barcode_data, writer=ImageWriter())
    # Construct the file path relative to MEDIA_ROOT
    barcode_filename = f"{order_id}.png"
    barcode_path = os.path.join("barcodes", barcode_filename)
    # Save the barcode image
    barcode_full_path = os.path.join(settings.MEDIA_ROOT, barcode_path)
    code128.save(barcode_full_path)
    return barcode_path
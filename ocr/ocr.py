# This code is using the Python programming language to perform optical character recognition (OCR) on
# an image file named 'image1.png'.
from PIL import Image

import pytesseract

# Printing the output of the OCR to the console
print(pytesseract.image_to_string(Image.open('image1.png')))

from PIL import Image

import pytesseract

#print(pytesseract.image_to_string(Image.open('image.png')))
#print(pytesseract.image_to_string(Image.open('image2.png')))

#print(pytesseract.image_to_string(Image.open('test.png')))
#print(pytesseract.image_to_string(Image.open('test3.png')))
#print(pytesseract.image_to_string(Image.open('test4.png')))

#print(pytesseract.image_to_string(Image.open('test2.png')))
print(pytesseract.image_to_string(Image.open('skills.png')))
from pdf2image import convert_from_path
import pytesseract
import os

base_path = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_path, 'document.pdf')

pages = convert_from_path(pdf_path)

for page in pages:
    text = pytesseract.image_to_string(page)
    print(text)
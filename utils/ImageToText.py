from PIL import Image
import os
import sys
import pytesseract


def text_from_image(img, file_name):
    with open(file_name, "w") as f:
        text = pytesseract.image_to_string(img, lang="eng")
        f.write(text)
    return text

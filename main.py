from utils.ImageToText import text_from_image
from PIL import Image
if __name__ == "__main__":
    image_path = "/home/devbox/refrigeratorMonitor/tests/ImageTotext/test1.jpg"
    img = Image.open(image_path) 
    fileName = "/home/devbox/refrigeratorMonitor/text"
    text_from_image(img, fileName)

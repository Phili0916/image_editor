from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'unedited_images'
path_out = 'edited_images'

for photo in os.listdir(path):
    image = Image.open(f"{path}/{photo}")
    print(image.format, image.size, image.mode)

    edit = image.filter(ImageFilter.SHARPEN).rotate(-90)
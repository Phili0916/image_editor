from PIL import Image, ImageEnhance, ImageFilter, ImageChops
import os

path = './unedited_images'
edited_path = './edited_images'

for photo in os.listdir(path):
    image = Image.open(f"{path}/{photo}")
    # print(image.format, image.size, image.mode)

    edit = image.filter(ImageFilter.SHARPEN).rotate(-90)
    print(f"edit{edit}")

    ## Create a New Image
    new_image = Image.new('RGBA', (1000, 600))
    new_image.show()

    ## Color enhancer
    color_enhancer = ImageEnhance.Color(image)
    print(f"color_enhancer: {color_enhancer}")
    color_enhancer.enhance(5.0)
    color_enhancer.image.save(f"{edited_path}/color_enhanced_photo.jpg")


    ## Contrast enhancer
    contrast_enhancer = ImageEnhance.Contrast(image)
    contrast_enhancer.enhance(5.0).show()

    ## Brightness enhancer
    brightness_enhancer = ImageEnhance.Brightness(image)
    brightness_enhancer.enhance(1.5).show()

    ## Sharpness enhancer
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    sharpness_enhancer.enhance(5.0).show()
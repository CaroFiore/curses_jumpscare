from PIL import Image

def resize_image(image_path : str, x,y):
    img = Image.open(image_path)
    return img.resize((x,y))

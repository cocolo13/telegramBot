from rembg import remove
from PIL import Image


def remove_back(input_path, output_path):
    open_image = Image.open(input_path)
    done = remove(open_image)
    done.save(output_path)

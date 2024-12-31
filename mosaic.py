import random
from PIL import Image
import numpy as np

# Parameters

WIDTH = 15
HEIGHT = 15
SCALE_FACTOR = 100

def initialize(height, width):
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def scale(image, height, width, scale_factor):
    return image.resize((width * scale_factor, height * scale_factor), Image.NEAREST)

if __name__ == '__main__':
    mosaic = initialize(HEIGHT, WIDTH)

    image = Image.fromarray(mosaic, 'RGB')
    image = scale(image, HEIGHT, WIDTH, SCALE_FACTOR)
    image.save('images/output.png')

    image.show()

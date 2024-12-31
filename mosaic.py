import random
from PIL import Image
import numpy as np
from mse import mse
import cv2
import os

# Parameters -----------------------------------------------------------------------------------------

WIDTH = 15
HEIGHT = 15
SCALE_FACTOR = 100
POPULATION_SIZE = 100
GENERATIONS = 500

# Genetic algorithm functions ------------------------------------------------------------------------

def initialization(height, width):
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# def selection():

# def mutation():

# def crossover():

def fitness(image, original):
    return mse(image, original)

# Image functions ------------------------------------------------------------------------------------
    
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
            width, height = img.size
            return height, width

def get_image_path():
    file_name = input("Enter image name: ")
    image_path = f"images/{file_name}.jpg"

    # Check if the file exists
    if not os.path.isfile(image_path):
        print("The file does not exist")
        return

    return image_path

def scale_image(image, height, width, scale_factor):
    return image.resize((width * scale_factor, height * scale_factor), Image.NEAREST)

# Main -----------------------------------------------------------------------------------------------

if __name__ == '__main__':

    image_path = get_image_path()
    height, width = get_image_dimensions(image_path)
    print(f" Height: {height} Width: {width}")

    mosaic = initialization(height // 30, width // 30)

    image = Image.fromarray(mosaic, 'RGB')
    image = scale_image(image, height, width, 1)
    image.save('output/output.png')

    image.show()

    fitness_value = fitness(cv2.imread('output/output.png'), cv2.imread('images/panda.jpg'))

    print(f"Fitness value: {fitness_value}")


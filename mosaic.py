import random
from PIL import Image
import numpy as np
from mse import mse
import cv2
import os

# Parameters -----------------------------------------------------------------------------------------

POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01

# Genetic algorithm functions ------------------------------------------------------------------------

def generate_random_mosaic(height, width):
     return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def initialization(height, width, population_size):
    return[generate_random_mosaic(height, width) for _ in range(population_size)]

# Randomly select 'tournament_size' individuals and return the one with the best fitness
def selection(population, fitness_array, tournament_size=5):
    selected = random.sample(list(zip(population, fitness_array)), tournament_size)
    selected.sort(key=lambda x: x[1]) 
    return selected[0][0]

def mutation(image, mutation_rate=0.01):
    height, width, _ = image.shape
    mutated_image = image.copy()

    for i in range(height):
        for j in range(width):
            if random.random() < mutation_rate:
                mutated_image[i, j] = np.random.randint(0, 256, 3, dtype=np.uint8)  # Random RGB value

    return mutated_image

def crossover(parent1, parent2):
    # Choose a random point to crossover
    height, width, _ = parent1.shape
    crossover_point = random.randint(1, height - 1)

    offspring1 = np.vstack((parent1[:crossover_point, :, :], parent2[crossover_point:, :, :]))
    offspring2 = np.vstack((parent2[:crossover_point, :, :], parent1[crossover_point:, :, :]))

    return offspring1, offspring2

def fitness(image, original):
    return mse(image, original)

# Image functions ------------------------------------------------------------------------------------

# TODO: Simplify
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

def scale_image(image, height, width, scale_factor=1):
    return image.resize((width * scale_factor, height * scale_factor), Image.NEAREST)

# Main genetic algorithm loop
def run_genetic_algorithm(population, fitness_array, generations=500):
    for generation in range(generations):
        print(f"Generation {generation+1}/{generations}")

        new_population = []

        # Apply selection, crossover, and mutation
        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population, fitness_array)
            parent2 = selection(population, fitness_array)

            # Crossover
            offspring1, offspring2 = crossover(parent1, parent2)

            # Mutation
            offspring1 = mutation(offspring1)
            offspring2 = mutation(offspring2)

            # Add offspring to the new population
            new_population.append(offspring1)
            if len(new_population) < POPULATION_SIZE:
                new_population.append(offspring2)

        # Update the population
        population = new_population

        # TODO: Encapsulate in its own function

        # Calculate fitness for the new population
        fitness_array = []
        for mosaic in population:
            image = Image.fromarray(mosaic, 'RGB')
            image = scale_image(image, height, width)
            image_array = np.array(image)
            fitness_value = fitness(image_array, cv2.imread(image_path))
            fitness_array.append(fitness_value)

        best_fitness = min(fitness_array)
        best_index = fitness_array.index(best_fitness)
        best_solution = population[best_index]

        # Save every 10 generations
        if generation % 10 == 0:
            best_image = Image.fromarray(best_solution, 'RGB')
            best_image = scale_image(best_image, height, width, 1)
            best_image.save(f"output/gen_{generation+1}.png")

    return best_solution


# Main -----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    image_path = get_image_path()
    height, width = get_image_dimensions(image_path)
    print(f"Height: {height} Width: {width}")

    # Initial population
    population = initialization(height // 10, width // 10, POPULATION_SIZE)

    # Calculate initial fitness
    fitness_array = []
    for mosaic in population:
        image = Image.fromarray(mosaic, 'RGB')
        image = scale_image(image, height, width, 1)
        image_array = np.array(image)
        fitness_value = fitness(image_array, cv2.imread(image_path))
        fitness_array.append(fitness_value)

    # Run genetic algorithm
    best_mosaic = run_genetic_algorithm(population, fitness_array, GENERATIONS)

    # Final output
    best_image = Image.fromarray(best_mosaic, 'RGB')
    best_image = scale_image(best_image, height, width, 1)
    best_image.save('output/final_mosaic.png')
    best_image.show()



import sys
import time
import random
import operator

from utils import *
from population import *
from fitness import compute_population_fitness

# Utility function that checks if an individual matches the chosen word
# If that happens the index of the individual is returned, if not -1 is
# returned
def check_for_matching_word(population, word_to_match):
    for i in range(0, len(population)):
        if population[i] == word_to_match:
            return i
    
    return -1

if len(sys.argv) < 3:
    print("Usage: python word_generator.py <initial_population> <mutation_rate> <verbose>\n")
    print("Initial population: an integer representing the initial population for the algoritm.")
    print("Mutation rate: a float in the range [0.0, 1.0] that represents the probability a newborn individual is mutated.")
    print("Verbose: a string ('y' or 'n') that indicates whether the logs produced by the program should be verbose.")

    sys.exit()

test_word = "hello world"

start_time = time.time()

generation = 1
word_length = len(test_word)

verbose = sys.argv[3] == 'y'
population_size = int(sys.argv[1])
mutation_rate = float(sys.argv[2])

population = generate_population(population_size, word_length)
target_individual_index = check_for_matching_word(population, test_word)

while target_individual_index == -1:
    fitnesses = compute_population_fitness(population, test_word)
    individuals_for_breeding = elitist_selection(fitnesses, int(population_size / 2), min([5, population_size / 5]))
    
    new_generation = create_children(individuals_for_breeding, population_size)
    
    population = mutate_population(new_generation, mutation_rate)

    if verbose:
        print("Fittest individual (Generation " + str(generation) + "): " + population[0])

    generation += 1
    target_individual_index = check_for_matching_word(population, test_word)

if verbose:
    print("Fittest individual (Generation " + str(generation) + "): " + population[target_individual_index])

time_elapsed = time.time() - start_time
print(str(population_size) + ", " + str(generation) + ", " + str(mutation_rate) + ", " + str(time_elapsed))
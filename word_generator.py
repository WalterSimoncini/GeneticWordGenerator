import sys
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

test_word = "hello world"

generation = 1
population_size = 200
word_length = len(test_word)
population = generate_population(population_size, word_length)
target_individual_index = check_for_matching_word(population, test_word)

while target_individual_index == -1:
    fitnesses = compute_population_fitness(population, test_word)
    individuals_for_breeding = elitist_selection(fitnesses, int(population_size / 3), 10)
    
    new_generation = create_children(individuals_for_breeding, population_size)
    population = mutate_population(new_generation, 0.3)
    
    print("Fittest individual (Generation " + str(generation) + "): " + population[0])

    generation += 1
    target_individual_index = check_for_matching_word(population, test_word)

print("Fittest individual (Generation " + str(generation) + "): " + population[target_individual_index])
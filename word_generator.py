import sys
import time
import random

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

# If not enough command line arguments are given by the user the program
# will print an help text and quit
if len(sys.argv) < 3:
    print("Usage: python word_generator.py <initial_population> <mutation_rate> <verbose>\n")
    print("Initial population: an integer representing the initial population for the algoritm.")
    print("Mutation rate: the chance a newborn individual is mutated. Must be a float in the range [0, 1]")
    print("Verbose: a string ('y' / 'n') that indicates whether the logs should be verbose.")
    
    sys.exit()

test_word = "hello world"

start_time = time.time()

generation = 1
word_length = len(test_word)

verbose = sys.argv[3] == 'y'
population_size = int(sys.argv[1])
mutation_rate = float(sys.argv[2])

# Generate the initial population and check if one individuals matches the target word
population = generate_population(population_size, word_length)
target_individual_index = check_for_matching_word(population, test_word)

# Until a matching individual is found repeat the breeding process
while target_individual_index == -1:
    # Compute the population's fitness and select the individuals that will give birth
    # to the next generation
    fitnesses = compute_population_fitness(population, test_word)
    individuals_for_breeding = elitist_selection(fitnesses, max([int(population_size / 10), 2]))
    
    # Give birth to children for the next generation
    new_generation = create_children(individuals_for_breeding, population_size)
    # Carry over the mutation operation over the population with respect to the
    # mutation rate (a.k.a how likely is mutation for an individual)
    population = mutate_population(new_generation, mutation_rate)

    if verbose:
        print("Fittest individual (Generation " + str(generation) + "): " + population[0])

    generation += 1
    # Check if an individual matches the target word
    target_individual_index = check_for_matching_word(population, test_word)

if verbose:
    print("Fittest individual (Generation " + str(generation) + "): " + population[target_individual_index])

time_elapsed = time.time() - start_time

# Log the relevant information about this run of the genetic algorithm in a way
# that is easy to parse for a performance evaluation program
print(str(population_size) + ", " + str(generation) + ", " + str(mutation_rate) + ", " + str(time_elapsed))
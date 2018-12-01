import sys
import pprint
import random
from utils import *

# Generates a new individual with the input length
# using random lowercase letters and symbols
def generate_individual (length):
    result = ""

    for _ in range(0, length):
        result += generate_letter()
    
    return result

# Generates a population of the specified size where individuals
# have all a fixed word length specified as an input argument
def generate_population (population_size, word_length):
    population = []

    for _ in range(0, population_size):
        population.append(generate_individual(word_length))
    
    return population

# Creates a new children by taking half of the genes
# from parent A and half of the genes from parent B
# using a splitting point in the middle of the chromosome
def create_child_mid_crossover (parent_a, parent_b):
    child = ""

    for i in range(0, len(parent_a)):
        if i < int(len(parent_a) / 2):
            child += parent_a[i]
        else:
            child += parent_b[i]

    return child

# Simulates breeding by returning the genotype belonging
# to one of the two parents. This function is useful to
# test the influence of crossover on the genetic algorithm
def create_child_copy_parent (parent_a, parent_b):
    return random.choice([parent_a, parent_b])

# Simulates breeding with the input breeders until the specified
# number of children is born. Breeders are selected randomly from
# the input set
def create_children (breeders, children_count):
    next_population = []

    for j in range(children_count):
        # Select two random breeders and generate a new child 
        # using the crossover method
        couple = random.sample(breeders, 2)
        next_population.append(create_child_mid_crossover(couple[0], couple[1]))
        
    return next_population

# Randomly mutate a single gene (character) of the input individual
def mutate (individual):
    # Choose a random gene
    idx = int(random.random() * len(individual))

    characters = list(individual)
    # Mutate the target gene
    characters[idx] = generate_letter()

    return "".join(characters)

# Apply the mutation operation over a population. For every individual
# a random value is drawn and if the value is less than the mutation
# chance a mutation operation will be carried on the individual
def mutate_population (population, mutation_chance):
    for i in range(len(population)):
        if random.random() < mutation_chance:
            population[i] = mutate(population[i])
    
    return population

# Select the fittest individuals from the population
def elitist_selection(population, fit_count):
    # Sort the individuals by their fitness
    sorted_population = sorted(population, reverse = True, key = lambda tup: tup[1])
    fittest_individuals = []

    for i in range(fit_count):
        fittest_individuals.append(sorted_population[i][0])

    return fittest_individuals
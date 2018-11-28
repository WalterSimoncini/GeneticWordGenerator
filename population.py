import sys
import pprint
import random
from utils import *

def generate_individual (length):
    result = ""

    for _ in range(0, length):
        result += generate_letter()
    
    return result

def generate_population (population_size, word_length):
    population = []

    for _ in range(0, population_size):
        population.append(generate_individual(word_length))
    
    return population

# Creates a new children by taking half of the genes
# from parent A and half of the genes from parent B
# using a splitting point at the middle of the chromosome
def create_child_mid_crossover (parent_a, parent_b):
    child = ""

    for i in range(0, len(parent_a)):
        if i < int(len(parent_a) / 2):
            child += parent_a[i]
        else:
            child += parent_b[i]

    return child

def create_child_copy_parent (parent_a, parent_b):
    return random.choice([parent_a, parent_b])

# Creates a new children by selecting randomly a gene from
# parent A or parent B for every gene of the newborn child
def create_children (breeders, children_count):
    next_population = []

    for j in range(children_count):
        couple = random.sample(breeders, 2)
        next_population.append(create_child_mid_crossover(couple[0], couple[1]))
        
    return next_population

def mutate (individual):
    idx = int(random.random() * len(individual))

    characters = list(individual)
    characters[idx] = generate_letter()

    return "".join(characters)

def mutate_population (population, mutation_chance):
    for i in range(len(population)):
        if random.random() < mutation_chance:
            population[i] = mutate(population[i])
    
    return population

def elitist_selection(sorted_population, fit_count):
    next_gen = []

    for i in range(fit_count):
        next_gen.append(sorted_population[i][0])
    
    random.shuffle(next_gen)

    return next_gen
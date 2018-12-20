import sys
import pprint

# Compute the fitness of an individual. The fitness is computed as the number
# of matching letters between the individual and the target word. The fitness
# is then normalized to a float value between 0 and 1. If the individual and
# the target word have different lengths -1 is returned.
def fitness (word, word_to_match):
    if (len(word) != len(word_to_match)):
        print("Words have different lengths")

        return -1
    else:
        score = 0

        # Compute the number of matching letters between the 
        # individual and the target word
        for i in range(0, len(word_to_match)):
            if (word[i] == word_to_match[i]):
                score += 1

        # Normalize the fitness to a value between 0 and 1
        return score / float(len(word_to_match))

# Compute the fitnesses of a whole population and return them as a tuple
# in the format (individual, fitness).
def compute_population_fitness(population, word_to_match):
    fitnesses = []

    # Compute the fitness for every individual in the population and build
    # the resulting tuples
    for individual in population:
        individual_tuple = tuple([individual, fitness(word_to_match, individual)]);
        fitnesses.append(individual_tuple)

    return fitnesses
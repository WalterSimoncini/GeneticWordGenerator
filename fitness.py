import sys
import pprint

def fitness (word, word_to_match):
    if (len(word) != len(word_to_match)):
        print("Words have different lengths")

        return -1
    else:
        score = 0

        for i in range(0, len(word_to_match)):
            if (word[i] == word_to_match[i]):
                score += 1

        # Normalize the fitness to values between 0 and 1
        return score / float(len(word_to_match))

def compute_population_fitness(population, word_to_match):
    fitnesses = []

    # print("P: " + str(len(population)))

    for individual in population:
        individual_tuple = tuple([individual, fitness(word_to_match, individual)]);
        fitnesses.append(individual_tuple)

    sorted_individuals = sorted(fitnesses, reverse = True, key = lambda tup: tup[1])

    #print("Sorted: " + str(sorted_individuals))
    
    return sorted_individuals
import random
import operator

def generate_word (length):
    result = ""

    for i in range(0, len(word_to_match)):
        letter = chr(97 + int(26 * random.random()))
        result += letter
    
    return result

def generate_population (size, word_to_match):
    population = []

    for i in range(0, size):
        population.append(generate_word(len(word_to_match)))
    
    return population

def fitness (word, word_to_match):
    if (len(word) != len(word_to_match)):
        print("Words have different lengths")
        return
    else:
        score = 0

        for i in range(0, len(word_to_match)):
            if (word[i] == word_to_match[i]):
                score += 1

        return score * 100 / len(word_to_match)

def compute_population_fitness(population, word_to_match):
    fitnesses = {}

    for individual in population:
        fitnesses[individual] = fitness(word_to_match, individual)

    return sorted(population.items(), key = operator.itemgetter(1), reverse = True)
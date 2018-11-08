import random
import operator

def generate_word (length):
    result = ""

    for i in range(0, length):
        delta = int(26 * random.random())
        letter = chr(97 + delta)

        result += letter
    
    return result

def generate_population (population_size, word_length):
    population = []

    for i in range(0, population_size):
        population.append(generate_word(word_length))
    
    return population

def fitness (word, word_to_match):
    if (len(word) != len(word_to_match)):
        print("Words have different lengths")

        return -1
    else:
        score = 0

        for i in range(0, len(word_to_match)):
            if (word[i] == word_to_match[i]):
                score += 1

        return score

def compute_population_fitness(population, word_to_match):
    fitnesses = {}

    for individual in population:
        fitnesses[individual] = fitness(word_to_match, individual)

    return sorted(fitnesses.iteritems(), key = lambda (k,v): (v,k), reverse = True)

def select_from_population(sorted_population, fit_count, unfit_count):
    next_gen = []

    for i in range(fit_count):
        next_gen.append(sorted_population[i][0])

    for i in range(unfit_count):
        next_gen.append(random.choice(sorted_population)[0])
    
    random.shuffle(next_gen)

    return next_gen

def create_child (parent_a, parent_b):
    child = ""

    for i in range(len(parent_a)):
        if (int(100 * random.random()) < 50):
            child += parent_a[i]
        else:
            child += parent_b[i]
        
    return child

def create_children(breeders, children_count):
    next_population = []

    for i in range(len(breeders) / 2):
        for j in range(children_count):
            next_population.append(create_child(breeders[i], breeders[len(breeders) - 1 - i]))
    
    return next_population

def mutate(child):
    idx  = int(random.random() * len(child))

    if (index_modification == 0):
        word = chr(97 + int(26 * random.random())) + word[1:]
    else:
        word = word[:idx] + chr(97 + int(26 * random.random())) + word[idx+1:]
	
    return word

def mutate_population (population, mutation_chance):
    for i in range(len(population)):
        if random.random() < mutation_chance:
            population[i] = mutate[population[i]]
    
    return population
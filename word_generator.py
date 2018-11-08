import random
import operator

def coin_flip ():
    return random.random() < 0.5

def generate_letter ():
    characters_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '?', '!', ',', '.']
    idx = int(random.random() * len(characters_table))

    return characters_table[idx]

def generate_word (length):
    result = ""

    for _ in range(0, length):
        result += generate_letter()
    
    return result

def generate_population (population_size, word_length):
    population = []

    for _ in range(0, population_size):
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
        if (coin_flip):
            child += parent_a[i]
        else:
            child += parent_b[i]
        
    return child

def create_children (breeders, children_count):
    next_population = []

    for i in range(len(breeders) / 2):
        for j in range(children_count):
            next_population.append(create_child(breeders[i], breeders[len(breeders) - 1 - i]))
    
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

def check_for_matching_word(population, word_to_match):
    for word in population:
        if word == word_to_match:
            return True
    
    return False


test_word = "sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium."
population_size = 200

word_length = len(test_word)
population = generate_population(population_size, word_length)
generation = 1

while not check_for_matching_word(population, test_word):
    fitnesses = compute_population_fitness(population, test_word)
    
    individuals_for_breeding = select_from_population(fitnesses, int(population_size / 3), 5)
    
    new_generation = create_children(individuals_for_breeding, population_size)
    population = mutate_population(new_generation, 0.3)
    
    print("Fittest individual (Generation " + str(generation) + "): " + population[0])

    generation += 1

print("Fittest individual (Generation " + str(generation) + "): " + population[0])
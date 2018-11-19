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

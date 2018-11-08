import random

def coin_flip ():
    return random.random() < 0.5

def generate_letter ():
    characters_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '?', '!', ',', '.']
    idx = int(random.random() * len(characters_table))

    return characters_table[idx]
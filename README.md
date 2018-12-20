# Genetic word generator

A simple program that tries to generate the string "hello world" using genetic algorithms. To run the program use:

`python word_generator.py <population_size> <mutation_rate> <verbose>`

Where:

- `<population_size>` is the size of the initial population (e.g. 50)
- `<mutation_rate>` is the chance an individual will be mutated (a decimal number between 0.0 and 1.0)
- `<verbose>` whether the program should output the fittest individual of every generation or only information about the run in the format `population_size, number_of_generations, mutation_rate, time_elapsed` ('y' for verbose or 'n' for not verbose)

For example, you may run the program with `python word_generator.py 50 0.3 y`

### Requirements

In case you want to recreate the charts in the `charts` folder you might have to install the libraries listed in `requirements.txt`. No libraries should be needed for running the genetic algorithm. The program should work with both python 2.x and python 3.x. To use the plotting tools Python 2.x is recommended
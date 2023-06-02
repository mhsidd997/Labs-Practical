import random
from deap import base
from deap import creator
from deap import tools

# Define the equation: 5x^3 - 6x^2 + 8x = 1
equation = lambda x: 5 * x**3 - 6 * x**2 + 8 * x

# Define the problem representation
num_genes = 4 # Number of coefficients [a, b, c, d]
gene_range = (-10, 10) # Range for random gene initialization

# Define genetic algorithm parameters
population_size = 100
max_generations = 100
mutation_rate = 0.1
# Define the fitness function
def fitness(individual):
    # Evaluate the equation for the individual's coefficients
    x = 1 # Value of x for equation evaluation
    result = individual[0] * x**3 + individual[1] * x**2 + individual[2] * x + individual[3]
    return abs(result - 1)

# Generate an initial population
population = []
for _ in range(population_size):
    individual = [random.uniform(*gene_range) for _ in range(num_genes)]
    population.append(individual)

# Main genetic algorithm loop
for generation in range(max_generations):
    # Evaluate fitness for each individual in the population
    fitness_scores = [fitness(individual) for individual in population]
    
    # Select individuals for reproduction
    selected_indices = random.choices(range(population_size), k=population_size // 2,
    weights=fitness_scores)

# Create offspring through crossover and mutation
offspring = []
for i in range(0, len(selected_indices), 2):
    parent1 = population[selected_indices[i]]
    parent2 = population[selected_indices[i+1]]
    
    # Perform one-point crossover
    crossover_point = random.randint(1, num_genes - 1)
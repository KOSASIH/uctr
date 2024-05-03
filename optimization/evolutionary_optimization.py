import random
import math

class EvolutionaryOptimization:
    def __init__(self, objective_function, population_size, mutation_rate, num_generations):
        self.objective_function = objective_function
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def initialize_population(self):
        self.population = [random.random() for _ in range(self.population_size)]

    def evaluate_population(self):
        self.fitness = [self.objective_function(individual) for individual in self.population]

    def select_parents(self):
        total_fitness = sum(self.fitness)
        probabilities = [fitness / total_fitness for fitness in self.fitness]
        parents = random.choices(self.population, weights=probabilities, k=self.population_size)
        return parents

    def mutate_population(self):
        mutated_population = []
        for individual in self.population:
            if random.random() < self.mutation_rate:
                mutated_individual = individual + random.uniform(-0.1, 0.1)
                mutated_population.append(max(min(mutated_individual, 1.0), 0.0))
            else:
                mutated_population.append(individual)
        self.population = mutated_population

    def run(self):
        self.initialize_population()
        for _ in range(self.num_generations):
            self.evaluate_population()
            parents = self.select_parents()
            self.population = parents
            self.mutate_population()
        best_individual = max(self.population, key=lambda x: self.objective_function(x))
        return best_individual

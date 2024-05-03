import random
import math

class Particle:
    def __init__(self, position, velocity, personal_best, personal_best_fitness):
        self.position = position
        self.velocity = velocity
        self.personal_best = personal_best
        self.personal_best_fitness = personal_best_fitness

class ParticleSwarmOptimization:
    def __init__(self, objective_function, population_size, num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight):
        self.objective_function = objective_function
        self.population_size = population_size
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.inertia_weight = inertia_weight
        self.cognitive_weight = cognitive_weight
        self.social_weight = social_weight

    def initialize_population(self):
        self.population = [Particle(random.random() for _ in range(self.population_size)), ] * self.num_particles
        self.global_best = min(self.population, key=lambda x: self.objective_function(x.position))
        self.global_best_fitness = self.objective_function(self.global_best.position)

    def update_particle(self, particle):
        r1, r2 = random.random(), random.random()
        cognitive_component = self.cognitive_weight * r1 * (particle.personal_best

import random
import numpy as np

class Particle:
    def __init__(self, position, velocity, personal_best, global_best):
        self.position = position
        self.velocity = velocity
        self.personal_best = personal_best
        self.global_best = global_best

class PSO:
    def __init__(self, dimensions, particles, iterations, w, c1, c2, lower_bound, upper_bound):
        self.dimensions = dimensions
        self.particles = particles
        self.iterations = iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def initialize_particles(self):
        self.particles = []
        for _ in range(self.particles):
            position = np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions)
            velocity = np.random.uniform(-1, 1, self.dimensions)
            personal_best = position.copy()
            personal_best_fitness = self.evaluate_fitness(position)
            global_best = personal_best.copy()
            global_best_fitness = personal_best_fitness
            particle = Particle(position, velocity, personal_best, global_best)
            self.particles.append(particle)

    def evaluate_fitness(self, position):
        # Evaluate the fitness based on the position
        pass

    def update_velocity(self, particle):
        r1, r2 = np.random.rand(2)
        cognitive_component = self.c1 * r1 * (particle.personal_best - particle.position)
        social_component = self.c2 * r2 * (particle.global_best - particle.position)
        particle.velocity = self.w * particle.velocity + cognitive_component + social_component

    def update_position(self, particle):
        particle.position += particle.velocity
        particle.position = np.clip(particle.position, self.lower_bound, self.upper_bound)

    def update_personal_best(self, particle):
        current_fitness = self.evaluate_fitness(particle.position)
        if current_fitness < particle.personal_best_fitness:
            particle.personal_best = particle.position.copy()
            particle.personal_best_fitness = current_fitness

    def update_global_best(self):
        global_best = min(particle.personal_best_fitness for particle in self.particles)
        global_best_position = min(particle.personal_best for particle in self.particles if particle.personal_best_fitness == global_best)
        self.global_best = global_best_position

    def run(self):
        self.initialize_particles()
        for _ in range(self.iterations):
            for particle in self.particles:
                self.update_velocity(particle)
                self.update_position(particle)
                self.update_personal_best(particle)
            self.update_global_best()
        return self.global_best

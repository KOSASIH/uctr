import math

class PhysicsSimulation:
    def __init__(self, initial_position, initial_velocity, initial_acceleration, time_step):
        self.position = initial_position
        self.velocity = initial_velocity
        self.acceleration = initial_acceleration
        self.time_step = time_step

    def update(self):
        self.velocity += self.acceleration * self.time_step
        self.position += self.velocity * self.time_step

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_acceleration(self):
        return self.acceleration

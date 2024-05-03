import math

class RobotSimulation:
    def __init__(self, initial_position, initial_orientation, initial_speed, initial_steering_angle, time_step):
        self.position = initial_position
        self.orientation = initial_orientation
        self.speed = initial_speed
        self.steering_angle = initial_steering_angle
        self.time_step = time_step

    def update(self):
        turn_radius = self.speed / self.steering_angle
        new_x = self.position[0] + self.speed * math.cos(self.orientation) * self.time_step
        new_y = self.position[1] + self.speed * math.sin(self.orientation) * self.time_step
        self.position = (new_x, new_y)
        self.orientation = (self.orientation + self.steering_angle * self.time_step) % (2 * math.pi)

    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation

    def get_speed(self):
        return self.speed

    def get_steering_angle(self):
        return self.steering_angle

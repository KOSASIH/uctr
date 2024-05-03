import time
import math

class Robot:
    def __init__(self, initial_position, initial_orientation):
        self.position = initial_position
        self.orientation = initial_orientation

    def move(self, distance, angle):
        # Convert angle to radians
        angle_rad = math.radians(angle)

        # Calculate new position
        new_x = self.position[0] + distance * math.cos(angle_rad)
        new_y = self.position[1] + distance * math.sin(angle_rad)

        # Update position
        self.position = (new_x, new_y)

    def rotate(self, angle):
        # Convert angle to radians
        angle_rad = math.radians(angle)

        # Update orientation
        self.orientation = (self.orientation[0] + angle_rad) % (2 * math.pi)

    def get_position(self):
        return self.position

    def get_orientation(self):
        return self.orientation

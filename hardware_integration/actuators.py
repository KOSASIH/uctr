class Actuator:
    def __init__(self):
        pass

    def write(self, value):
        # Write value to actuator
        pass

class Motor(Actuator):
    def write(self, speed):
        # Set motor speed
        pass

class Valve(Actuator):
    def write(self, state):
        # Set valve state
        pass

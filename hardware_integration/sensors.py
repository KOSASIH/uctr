class Sensor:
    def __init__(self):
        pass

    def read(self):
        # Read sensor data
        return 0

class TemperatureSensor(Sensor):
    def read(self):
        # Read temperature value
        return 25.0

class PressureSensor(Sensor):
    def read(self):
        # Read pressure value
        return 101325.0

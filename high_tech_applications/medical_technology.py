class MedicalDevice:
    def __init__(self):
        pass

    def read(self):
        # Read sensor data
        return 0

    def write(self, value):
        # Write value to actuator
        pass

class HeartRateMonitor(MedicalDevice):
    def read(self):
        # Read heart rate value
        return 60

class InsulinPump(MedicalDevice):
    def write(self, insulin_dose):
        # Set insulin dose
        pass

import OpenVR
import time

def main():
    # Initialize the OpenVR API
    vr = OpenVR.init()

    # Get the first available controller
    controller = vr.getController(0)

    # Main loop
    while True:
        # Get the controller state
        state = controller.getState()

        # Apply haptic

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

        # Apply haptic feedback
        if state.rTrigger > 0.5:
            controller.setHapticFeedback(0, 0.5, 500)
        else:
            controller.setHapticFeedback(0, 0, 0)

        # Wait for a second
        time.sleep(1)

if __name__ == '__main__':
    main()

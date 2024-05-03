import pygame
import pygame.camera
import pygame.image

def main():
    pygame.init()

    # Initialize the camera
    camera = pygame.camera.Camera(pygame.locals.CAMERA_LIST, (640, 480))
    camera.start()

    # Set up the display
    screen = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the camera image
        image = camera.get_image()

        # Display the camera image
        screen.blit(image, (0, 0))

        # Update the display
        pygame.display.flip()

    # Clean up
    camera.stop()
    pygame.quit()

if __name__ == '__main__':
    main()

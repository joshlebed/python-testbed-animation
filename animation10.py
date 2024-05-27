import numpy as np
import pygame
import sys

def generate_psychedelic_animation():
    # Initialize Pygame
    pygame.init()
    
    # Get the screen resolution
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h
    aspect_ratio = screen_width / screen_height

    # Set up the screen
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Psychedelic Animation')

    # Generate grid of points with the screen aspect ratio
    x = np.linspace(-2 * np.pi * aspect_ratio, 2 * np.pi * aspect_ratio, screen_width)
    y = np.linspace(-2 * np.pi, 2 * np.pi, screen_height)
    X, Y = np.meshgrid(x, y)

    clock = pygame.time.Clock()
    i = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the frame
        Z = np.sin(X**2 + Y**2 + i/10.0)

        # Normalize Z to the range 0-255
        Z_normalized = ((Z - Z.min()) / (Z.max() - Z.min()) * 255).astype(np.uint8)
        
        # Create a surface from the array
        surface = pygame.surfarray.make_surface(np.dstack([Z_normalized] * 3))
        
        # Scale the surface to the screen size
        surface = pygame.transform.scale(surface, (screen_width, screen_height))

        # Draw the surface to the screen
        screen.blit(surface, (0, 0))
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(20)
        
        # Increment frame counter
        i += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    generate_psychedelic_animation()

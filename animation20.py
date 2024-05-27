import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt

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
    direction = -1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

        # Calculate the frame with a galaxy-like spiral pattern
        R = np.sqrt(X**2 + Y**2)
        theta = np.arctan2(Y, X)
        Z = np.sin(5 * theta + R + i / 10.0)
        
        # Normalize Z to the range 0-1 for colormap mapping
        Z_normalized = (Z - Z.min()) / (Z.max() - Z.min())
        
        # Map normalized values to colors using a colormap
        colormap = plt.get_cmap('hsv')  # You can choose other colormaps like 'viridis', 'plasma', etc.
        colors = colormap(Z_normalized)

        # Convert colors to an 8-bit integer format (0-255)
        colors = (colors[:, :, :3] * 255).astype(np.uint8)
        
        # Create a surface from the array
        surface = pygame.surfarray.make_surface(colors)
        
        # Rotate the surface by 90 degrees
        rotated_surface = pygame.transform.rotate(surface, 90)
        
        # Draw the surface to the screen
        screen.blit(rotated_surface, (0, 0))
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(20)
        
        # Always decrement the frame counter
        i += direction

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    generate_psychedelic_animation()

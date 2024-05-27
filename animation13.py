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

    # Generate grid of points with correct aspect ratio
    size = 1000
    x = np.linspace(-2 * np.pi * aspect_ratio, 2 * np.pi * aspect_ratio, size)
    y = np.linspace(-2 * np.pi, 2 * np.pi, size)
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
        
        # Normalize Z to the range 0-1 for colormap mapping
        Z_normalized = (Z - Z.min()) / (Z.max() - Z.min())
        
        # Map normalized values to colors using a colormap
        colormap = plt.get_cmap('hsv')  # You can choose other colormaps like 'viridis', 'plasma', etc.
        colors = colormap(Z_normalized)

        # Convert colors to an 8-bit integer format (0-255)
        colors = (colors[:, :, :3] * 255).astype(np.uint8)
        
        # Create a surface from the array
        surface = pygame.surfarray.make_surface(colors)
        
        # Draw the surface to the screen with proper aspect ratio
        scaled_surface = pygame.transform.smoothscale(surface, (screen_width, screen_height))
        screen.blit(scaled_surface, (0, 0))
        
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

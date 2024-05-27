import numpy as np
import pygame
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

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

        # Calculate the number of arms, changing over time
        num_arms = 2 + int(3 * (np.sin(i / 200.0) + 1))  # Number of arms oscillates between 2 and 5
        num_arms = 9  # Uncomment this line to fix the number of arms to 8
        
        # Calculate the frame with a galaxy-like spiral pattern
        R = np.sqrt(X**2 + Y**2)
        theta = np.arctan2(Y, X)
        Z = np.sin(num_arms * theta + R + i / 10.0)
        
        # Normalize Z to the range 0-1 for colormap mapping
        Z_normalized = (Z - Z.min()) / (Z.max() - Z.min())

        # Create a smooth periodic hue shift within the cool color range
        hue_shift = (np.sin(i / 100.0) + 1) / 2  # Oscillates smoothly between 0 and 1
        colormap = mcolors.LinearSegmentedColormap.from_list('cool_hue', plt.cm.cool(np.linspace(hue_shift, hue_shift + 1, 256)))

        # Map normalized values to colors using the custom colormap
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

import numpy as np
import matplotlib.pyplot as plt

def generate_psychedelic_visuals():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Generate grid of points
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    X, Y = np.meshgrid(x, y)
    
    # Calculate the function values
    Z = np.sin(X**2 + Y**2)
    
    # Generate the plot
    ax.imshow(Z, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv', interpolation='bilinear')
    
    # Remove axis
    ax.axis('off')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    generate_psychedelic_visuals()

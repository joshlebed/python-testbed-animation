import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Function to update each frame of the animation
def generate_psychedelic_frame(i, X, Y, ax):
    Z = np.sin(X**2 + Y**2 + i/10.0)
    ax.clear()
    ax.imshow(Z, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv', interpolation='bilinear')
    ax.axis('off')

# Function to set up and run the animation
def generate_psychedelic_animation():
    # Get the screen size
    screen_width, screen_height = rcParams['figure.figsize'] = plt.figaspect(1)
    
    # Create the figure with the size of the screen
    fig, ax = plt.subplots(figsize=(screen_width, screen_height))
    
    # Generate grid of points
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    X, Y = np.meshgrid(x, y)
    
    # Create the animation
    ani = animation.FuncAnimation(fig, generate_psychedelic_frame, fargs=(X, Y, ax), frames=200, interval=50)
    
    # Set the figure to take up the entire screen
    fig.tight_layout(pad=0)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Display the animation
    plt.show()

if __name__ == "__main__":
    generate_psychedelic_animation()

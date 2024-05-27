import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update each frame of the animation
def generate_psychedelic_frame(i, X, Y, im):
    Z = np.sin(X**2 + Y**2 + i/10.0)
    im.set_array(Z)
    return [im]

# Function to set up and run the animation
def generate_psychedelic_animation():
    # Set the aspect ratio for widescreen (16:9)
    aspect_ratio = 16 / 9
    
    # Create the figure with the widescreen size
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Generate grid of points
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    X, Y = np.meshgrid(x, y)
    
    # Calculate the initial frame
    Z = np.sin(X**2 + Y**2)
    
    # Display the initial frame
    im = ax.imshow(Z, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv', interpolation='bilinear')
    
    # Remove axis and extra spaces
    ax.axis('off')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Create the animation
    ani = animation.FuncAnimation(fig, generate_psychedelic_frame, fargs=(X, Y, im), frames=200, interval=50, blit=True)
    
    # Display the animation
    plt.show()

if __name__ == "__main__":
    generate_psychedelic_animation()

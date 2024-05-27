import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

# Function to update each frame of the animation
def generate_psychedelic_frame(i, X, Y, im):
    Z = np.sin(X**2 + Y**2 + i/10.0)
    im.set_array(Z)
    return [im]

# Function to set up and run the animation
def generate_psychedelic_animation():
    # Get screen size using tkinter
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
    # Set the aspect ratio for widescreen (16:9)
    aspect_ratio = screen_width / screen_height
    
    # Create the figure with the screen size
    fig, ax = plt.subplots(figsize=(screen_width / 100, screen_height / 100), dpi=100)
    
    # Generate grid of points with the screen aspect ratio
    x = np.linspace(-2 * np.pi * aspect_ratio, 2 * np.pi * aspect_ratio, 1000)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    X, Y = np.meshgrid(x, y)
    
    # Calculate the initial frame
    Z = np.sin(X**2 + Y**2)
    
    # Display the initial frame
    im = ax.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], cmap='hsv', interpolation='bilinear')
    
    # Remove axis and extra spaces
    ax.axis('off')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Create the animation
    ani = animation.FuncAnimation(fig, generate_psychedelic_frame, fargs=(X, Y, im), frames=200, interval=50, blit=True)
    
    # Set the figure to full screen
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    
    # Display the animation
    plt.show()

if __name__ == "__main__":
    generate_psychedelic_animation()

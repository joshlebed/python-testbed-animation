import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_psychedelic_frame(i, X, Y, ax):
    Z = np.sin(X**2 + Y**2 + i/10.0)
    ax.clear()
    ax.imshow(Z, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi], cmap='hsv', interpolation='bilinear')
    ax.axis('off')

def generate_psychedelic_animation():
    fig, ax = plt.subplots(figsize=(8, 8))
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    X, Y = np.meshgrid(x, y)
    
    ani = animation.FuncAnimation(fig, generate_psychedelic_frame, fargs=(X, Y, ax), frames=200, interval=50)
    
    plt.show()

if __name__ == "__main__":
    generate_psychedelic_animation()

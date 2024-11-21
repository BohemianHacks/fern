import matplotlib.pyplot as plt
import random

def generate_barnsley_fern(num_points=100000):
    x, y = 0, 0
    points = []
    for _ in range(num_points):
        p = random.random()
        if p < 0.01:
            x, y = 0, 0.16 * y
        elif p < 0.08:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 0.16
        elif p < 0.15:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.04
        else:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 0.16
        points.append((x, y))

    plt.scatter(*zip(*points), s=1, color='green')
    plt.axis('off')
    plt.show()

generate_barnsley_fern()

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# set a style "fivethirtyeight"
plt.style.use('fivethirtyeight')

# Create empty lists
x_vals = []
y_vals = []

# Create a infinite iterable for index
index = count()

# function to load csv data
def animate(i):
    # import the csv data by pandas
    data = pd.read_csv("data.csv")
    x = data["x_value"]
    y1 = data["total_1"]
    y2 = data["total_2"]

    # Clean axes
    plt.cla()

    # Create plots
    plt.plot(x, y1, label="Channel 1")
    plt.plot(x, y2, label="Channel 2")

    # Update the legend
    plt.legend()
# Animating `matplotlib.animation.FuncAnimation(figure, function, interval=millisecond)`
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
# interval=1000 means update every second.

plt.tight_layout()
plt.show()

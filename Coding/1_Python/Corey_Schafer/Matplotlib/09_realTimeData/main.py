import random
import itertools
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Choose the display style
plt.style.use('fivethirtyeight')

# Create empty lists
x_vals = []
y_vals = []

# Infinite index
index = itertools.count()
# itertools.count(start,[step]) : count(10) --> 10 11 12 13 14 ...
# itertools.cycle(p0) : cycle('ABCD') --> A B C D A B C D ...
# itertools. repeat(element, [times]) : repeat(10, 3) --> 10 10 10
# It's nice to work with `list.appen(next())`

def animate(i):
    # To extend the x which is the index of the datas
    x_vals.append(next(index))
    # To collect the random integer from 0 to 5, including 0 and 5.
    y_vals.append(random.randint(0, 5))
    # `plt.cla()` to stop create brand new line every time.
    plt.cla()
    # What's plt.cla (https://blog.csdn.net/tz_zs/article/details/81393098)
    plt.plot(x_vals, y_vals)

# Animating `matplotlib.animation.FuncAnimation(figure, function, interval=millisecond)`
ani = FuncAnimation(plt.gcf(), animate, interval=100)
# interval=1000 means update every second.

plt.tight_layout()
plt.show()

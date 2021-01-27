import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle="solid")
# Connect the dots `linestyle="solid"`

plt.gcf().autofmt_xdate()
# gcf stand for Get the Current Figure, to make it easy to read.

date_format = mpl_dates.DateFormatter("%b, %d, %Y")
# use date format class by matplotlib.dates

plt.gca().xaxis.set_major_formatter(date_format)
# gca stand for Get the Current Axes,

plt.tight_layout()

plt.show()

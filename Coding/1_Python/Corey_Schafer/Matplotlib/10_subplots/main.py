import pandas as pd
from matplotlib import pyplot as plt
# purpose : break a data up to multiple plots on the same figure.

# plt.gcf()
# get a reference to the current figure
# plt.gca()
# get the current class matplotlib.axes.Axes instance.

# Set seaborn style
plt.style.use('seaborn')

# import data with pandas
data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# # Method #1
# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
# make multiple plots on the same window.
# # ax is a plot
# `sharex=True` and `sharey=True` to share x and y values

# # Method #2
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
# make multiple plots on the different windows.

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')
# Use `ax` instead of plt

# set legend
ax1.legend()

# set title and x,y labels
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
# Just keep the bottom one x label
ax1.set_ylabel('Median Salary (USD)')
# `ax.set_`

ax2.legend()

# ax2.set_title('Median Salary (USD) by Age')
# Just keep the top one title
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# automatic padding
plt.tight_layout()

plt.show()

fig1.savefig("fig1.png")
fig2.savefig("fig2.png")

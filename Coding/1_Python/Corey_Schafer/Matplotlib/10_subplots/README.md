# Multiple Datas

__*It's a way to create plots on the different axis. It may or may not show on the same window.*__

## KEY
```python
# fig, ax = plt.subplots()
ax.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax.legend()

ax.set_title('Median Salary (USD) by Age')
ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')
```
__*The key is make plt as an instance*__
Use `ax` instead of `plt`.
Replaced `plt.title()`, `plt.xlabel()` and `plt.ylabel()`
with `ax.set_title()`, `ax.set_xlabel()` and `ax.set_ylabel()`.


## Method #1
On the same figure
```python
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
```
`nrows=2`, stand for number of rows.
`ncols=1`, stand for number of columns.
The default value is 1

`sharex=True` and `sharey=True` to share x and y values


## Method #2
On the different figure
```python
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
```


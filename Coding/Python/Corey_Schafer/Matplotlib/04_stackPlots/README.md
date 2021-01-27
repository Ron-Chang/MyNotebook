# Stack Plots

## Stack Plots  
```python
labels = ["player1", "player2", "player3"]
colors = ["#35A8E3", "#FF658C", "#67F745"]

plt.stackplot(minutes, player1, player2, player3,
            labels=labels, colors=colors)
```

## Customize the legend's location

```python
plt.legend(loc="upper left")
```
or 

```python
plt.legend(loc=(0.07,0.05))
# (percentage, percentage)
```

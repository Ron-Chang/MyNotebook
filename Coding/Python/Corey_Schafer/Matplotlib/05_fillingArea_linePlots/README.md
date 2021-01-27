# Line Plots - Filling

- Fill the area
- Change the opacity(0-1)
- Set an overall median
- plt.fill_between(x, y1, y2=0, alpha=1)  
_y2 is set 0 by default, It means all the away down to the bottom_
- Add a condition with `where` method

## Area Filling

```python
plt.fill_between(ages, py_salaries, dev_salaries, label="Above Avg",
                 where=(py_salaries >= dev_salaries),
                 interpolate=True, alpha=0.5, color="#1C86FB")
```
Format:
_*`plt.fill_between(x, y1, y2=0, alpha=1)`*_

Add `interpolate=True` to fixed the gap issue.

Add `where=(py_salaries >= dev_salaries)` to set a aondition.

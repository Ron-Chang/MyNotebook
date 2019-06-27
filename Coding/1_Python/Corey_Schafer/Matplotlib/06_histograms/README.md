# Histograms
__*Similar as a bar chart, but it collect a range of value as a bin.*__

# Sample (main.py)

```python
plt.hist(ages, bins=bins, edgecolor="black")
```
- Customize the bins range
- Add the edge color

# Import Data (real_sample.py)

```python
plt.hist(ages, bins=bins, edgecolor="black", log=True)
plt.axvline(median_age, color="#FF2229", label="Age Median", linewidth=2)
```
- Use `log = True` to show the mior data
- Add a midian line by `plt.axvline()`

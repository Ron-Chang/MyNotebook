# Scatter Plot
__*To show the relationship between two different values.*__

## Sample (main.py)
```python
plt.scatter(x, y, s=sizes, c=colors, cmap="Greens", marker="o",
            edgecolor="#F8547B", linewidth=1, alpha=0.9)
```

- Change the dots size by `s=100`, `s=[list]`.
- Change the dots colour by `c="black"`, `c=[list]` to mark different dots.
- `cmap="Greens"` to customize the style of dots.
- Change the dots marker by `marker="x"`.
- `edgecolor="#F8547B"` to change edge colour.
- `linewidth=1` to change edge width.
- `alpha=0.75` to change marker opacity.

```python
plt.scatter(view_count, likes, c=ratio, cmap="summer",
            edgecolor="black", linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label("Like/ Dislike Ratio")

plt.xscale("log")
plt.yscale("log")
```

- Use log method to solve a separated data
- Set a colour bar.

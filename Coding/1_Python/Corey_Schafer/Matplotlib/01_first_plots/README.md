# My First Plot  
- Build a `Virtual Enviroment`
- Resource the data from `list`
- Creat a `X-Y Plot`
- Create X,Y `labels` and a `Title`.
- Make a `legend` for each line
- Know how to set `Format` for each line
- Set `Styles`
- tragger `Grid`
- Auto save the `png` file in the current folder.

## Import  

```python
from matplotlib import pyplot as plt
```
`plt` is a general abbreviation for `pyplot`

## Format  

```python
plt.plot(dev_x, dev_y, color="blue", linestyle="--", marker=".", label="dev")
```

eaquals

```python
plt.plot(dev_x, dev_y, "b--.", label="dev")
```

## Styles  

```python
print(plt.style.available)
# Check out all available styles

plt.style.use("fivethirtyeight")
# 538 style

plt.style.use("ggplot")
# ggplot style

plt.xkcd()
# Cartoon style method
```

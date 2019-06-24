# Bar Chart & CSV

- How to make a `Bar Chart`
- `Separate` mutilple bar through `numpy`
- To shift the label number with `xticks` method
- To know how to import the data from `csv` file
- How to load the data by `csv` and `pandas`
- Counting the number by `Counter`
- Change the bar chart direction through `barh` method

## Bar Chart

```python
plt.bar(ages_x , py_dev_y, width=width, color="#073EF1", label="Python")
```
Useing `bar`( or `barh` to make a horizontal version) method instead of `plot`.

## Separate

```python
from matplotlib import pyplot as plt
import numpy as np

ages_x = [i for i in range(25,35+1)]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

x_indexes = np.arange(len(ages_x))
width = 0.25

plt.bar(x_indexes+width*(-0.5) , py_dev_y, width=width, label="Python")
plt.bar(x_indexes+width*(0.5), js_dev_y, width=width, label="JavaScript")
# plt.barh(width->height)

plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salarise (USD)")

plt.tight_layout()

plt.show()
```

## Import csv

There are multiple way to load the csv file, for instance,

- csv module from standard library
```python
# standard csv module
with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))
```

- read csv method from pandas
```python
# panda module
data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]
```
- load csv method from numpy etc.

## Counter

```python
language = []
popularity = []

for item in language_counter.most_common(10):
    language.append(item[0])
    popularity.append(item[1])
```
We can also make it through `zip` method.

```python
language,popularity = zip(*language_counter.most_common(10))
```


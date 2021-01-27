import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
ages = data["Age"]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor="black", log=True)
median_age = 29

# Use `log = True` to show the mior data

plt.axvline(median_age, color="#FF2229", label="Age Median", linewidth=2)

# Add a midian line by `plt.axvline()`

plt.legend()

plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")

plt.tight_layout()
plt.show()

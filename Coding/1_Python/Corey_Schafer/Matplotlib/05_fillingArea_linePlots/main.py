from matplotlib import pyplot as plt
import pandas as pd

# plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

plt.plot(ages, dev_salaries, color="#444444", label="All_Devs")

plt.plot(ages, py_salaries, color="#1C86FB",
    linestyle="--", linewidth=0.5, label="Python")
plt.plot(ages, js_salaries, color="#FFC628",
    linestyle="--", linewidth=0.5, label="Javascript")

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries, label="Above Avg",
                 where=(py_salaries >= dev_salaries), interpolate=True, alpha=0.5, color="#1C86FB")
plt.fill_between(ages, py_salaries, dev_salaries, label="Below Avg",
                 where=(py_salaries <= dev_salaries), interpolate=True, alpha=0.5, color="#EB1832")
# plt.fill_between(ages, js_salaries, overall_median,
#                  where=(js_salaries > overall_median), interpolate=True, alpha=0.25, color="#FFC628")
plt.fill_between(ages, js_salaries, overall_median, label="Belowo Median",
                 where=(js_salaries <= overall_median), interpolate=True, alpha=0.25, color="#40FF1C")


# # Fill the area
# # Change the opacity(0-1)
# # Set an overall median
# # Add a condition with `where` method to fill
# plt.fill_between(x, y1, y2=0, alpha=1)
# # y2 is set 0 by default, It means all the away down to the bottom
# # Add `interpolate=True` parameter to Fixed the gap issue
# interpolate=True

plt.legend()

plt.title("Median Salary (USD) by Age")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()

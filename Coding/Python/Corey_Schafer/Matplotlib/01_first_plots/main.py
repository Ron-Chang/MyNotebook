from matplotlib import pyplot as plt

# Check style
# print(plt.style.available)
plt.style.use("fivethirtyeight")
# plt.style.use("ggplot")

# Cartoon style method
# plt.xkcd()

dev_x = [i for i in range(25, 36)]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(dev_x, dev_y, color="#ffa159", linewidth=3, marker="o", label="All Devs")

py_dev_x = [i for i in range(29, 40)]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x, py_dev_y, color="b", marker="x", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(dev_x, js_dev_y, color="#3adedf", linestyle="--", marker=".", label="JavaScript")

plt.xlabel("Ages")
plt.ylabel("Median Salaries (USD)")
plt.title("Median Salary (USD) by Age")

plt.legend()

plt.grid(True)

plt.tight_layout()

# plt.savefig('plot.png')

plt.show()

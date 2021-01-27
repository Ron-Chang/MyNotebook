from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [i for i in range(1,10)]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ["player1", "player2", "player3"]
colors = ["#35A8E3", "#FF658C", "#67F745"]
plt.stackplot(minutes, player1, player2, player3,
            labels=labels, colors=colors)

# customize the location
plt.legend(loc="upper left")
# plt.legend(loc=(0.07,0.05))
# (percentage, percentage)

plt.title("My Stack Plot")
plt.tight_layout()
plt.show()

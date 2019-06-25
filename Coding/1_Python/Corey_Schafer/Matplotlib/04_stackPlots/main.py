from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [i for i in range(1,10)]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

plt.pie([1,1,1], labels=["Player 1", "Player 2", "Player 3"])

plt.title("My Stack Plot")
plt.tight_layout()
plt.show()

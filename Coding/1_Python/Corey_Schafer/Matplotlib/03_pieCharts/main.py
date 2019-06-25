from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60, 40, 30, 20]

labels = ['After Effect', 'Maya', 'PhotoShop', 'Illustrator']
colors = ['#7F239B', '#4A4A4A', '#332CFF', '#E6B30E']
explode = [0, 0.2, 0, 0]

plt.pie(slices, labels=labels, colors=colors, explode=explode, shadow=True,
        startangle=90, autopct="%1.1f%%", wedgeprops={'edgecolor':'black'})

plt.title("My Pie Chart")
plt.tight_layout()
plt.show()

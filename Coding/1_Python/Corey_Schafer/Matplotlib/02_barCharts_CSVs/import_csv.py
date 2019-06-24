import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
# Such as np, pd, plt are the conventions

plt.style.use("fivethirtyeight")

"""
multiple way to load the csv file
 - csv module from standard library
 - read csv method from pandas
 - load csv method from numpy
"""

# standard csv module
with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

# # panda module
data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

language = []
popularity = []

for item in language_counter.most_common(10):
    language.append(item[0])
    popularity.append(item[1])

# # we can make it through zip method as well
# language,popularity = zip(*language_counter.most_common(10))

print(language)
print(popularity)

# Chang the order direction
# we have to turn tuple into a list to reverse() through list() method
language.reverse()
popularity.reverse()

plt.barh(language, popularity)


plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()

import csv
import random
import time
# Purpose: Create a random real time data

# Set a start value
x_value = 0
total_1 = 1000
total_2 = 1000

# set header
fieldnames = ["x_value", "total_1", "total_2"]

# write the header as a new file "data.csv"
# (If the file existed, then overwrite it.)
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# Keep Loop(Infinite Loop)
while True:

    # Append the data into data.csv
    with open('data.csv', 'a') as csv_file:
        # write the data with Dictionary way(match the key)
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # info include the keys and values
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        # write info with writerow method
        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        # x_value equals ID (primary key)
        # when the function runs once x_value plus one
        x_value += 1

        # total_1 and total_2 random between the range
        # when the function runs once plus a random integer
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    # delay the process a second
    time.sleep(1)

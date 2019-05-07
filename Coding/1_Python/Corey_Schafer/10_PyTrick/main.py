def printInfo():

    print("_"*78)

    trick_01 = "    - 1. In short [if else] statement."
    trick_02 = "    - 2. Make a large number easy to read."
    trick_03 = "    - 3. Open a file with [Context Manager]."
    trick_04 = "    - 4. Packing a list with the index through [enumerate]."
    trick_05 = "    - 5. Packing two lists with [zip]."
    trick_06 = "    - 6. Unpacking values."
    trick_07 = "    - 7. Set dynamic attributes with [setattr] and [getattr]."
    trick_08 = "    - 8. Hide password input with [getpass]."
    trick_09 = "    - 9. Set a virtual enviroment to hide logging info."
    trick_10 = "    -10. Check documentation through [help()] or [dir()]."


    info = [
            trick_01, #trick_a
            trick_02, #trick_b
            trick_03, #trick_c
            trick_04, #trick_d
            trick_05, #trick_e
            trick_06, #trick_f
            trick_07, #trick_g
            trick_08, #trick_h
            trick_09, #trick_i
            trick_10] #trick_j

    for i in info:
        print(i)

    print()
    print("    -0. Input \"0\" to Extract.\n")
    print("_"*78)

def extract():
    print()
    print("*"*8+" Program has been terminate. "+"*"*8)
    print()
    quit()

def trick_a():
    x = """  - A:
condition = True
if condition:
    x = 1
else:
    x = 0
print(x)
# Output: 1
"""
    y = """  - B:
condition = True
x = 1 if condition else 0
print(x)
# Output: 1
"""
    result = """  - Conclusion:
if condition:    ==>    x = 1 if condition else 0
    x = 1
else:
    x = 0"""

    print(x)
    print(y)
    print(result)

def trick_b():

    num_1 = 10000000000
    num_2 = 100000000

    num_a = 10_000_000_000
    num_b = 100_000_000

    x = """  Underscore(_) is able to separate a great number.

num_1 = 10000000000
num_2 = 100000000

num_a = 10_000_000_000
num_b = 100_000_000
"""

    y = """
  Use \"f\" string to format a great number.

print(f'{num_1:,}')
# Output: 10,000,000,000
"""
    result_1 = "num_1 == num_a: {}".format(num_1 == num_a)
    result_2 = "num_2 == num_b: {}".format(num_2 == num_b)

    print(x)
    print(result_1)
    print(result_2)
    print(y)

def trick_c():

    x = """  - A:
f = open("test.txt", "r")

file_contents = f.read()

f.close()
"""
    y = """  - B:
with open("test.txt", "r") as f:
    file_contents = f.read()
"""
    result = """  - Conclusion:
f = open("test.txt", "r")    ==>    with open("test.txt", "r") as f:
file_contents = f.read()                file_contents = f.read()
f.close()"""

    print(x)
    print(y)
    print(result)

def trick_d():
    x = """  - A:
names = ["Ron","Chang","Trevor","Danny"]

index = 0
for name in names:
    print(index, name)
    index += 1
# Output:
0 Ron
1 Chang
2 Trevor
3 Danny
"""
    y = """  - B:
names = ["Ron","Chang","Trevor","Danny"]

for index, name in enumerate(names,start=1):
    print(index, name)
# Output:
1 Ron
2 Chang
3 Trevor
4 Danny
"""
    result = """  - Conclusion:
index = 0               ==>    for index, name in enumerate(names):
for name in names:                 print(index, name)
    print(index, name)
    index += 1"""

    print(x)
    print(y)
    print(result)

def trick_e():
    x = """  - A:
names = ["Ron","Chang","Trevor","Danny"]
heroes = ["Spiderman","Superman","Deadpool","Batman"]

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# Output:
Ron is actually Spiderman
Chang is actually Superman
Trevor is actually Deadpool
Danny is actually Batman
"""
    y = """  - B:
names = ["Ron","Chang","Trevor","Danny"]
heroes = ["Spiderman","Superman","Deadpool","Batman"]
universes = ["Marvel","DC","Marvel","DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# Output:
Ron is actually Spiderman from Marvel
Chang is actually Superman from DC
Trevor is actually Deadpool from Marvel
Danny is actually Batman from DC
"""
    extra = """  - Extra:
names = ["Ron","Chang","Trevor","Danny"]
heroes = ["Spiderman","Superman","Deadpool","Batman"]
universes = ["Marvel","DC","Marvel","DC"]

for value in zip(names, heroes, universes):
    print(value)

# Output:
('Ron', 'Spiderman', 'Marvel')
('Chang', 'Superman', 'DC')
('Trevor', 'Deadpool', 'Marvel')
('Danny', 'Batman', 'DC')
"""

    result = """  - Conclusion:
for index, name in enumerate(names):    ==>    for name, hero in zip(names, heroes):
    hero = heroes[index]                           print(f'{name} is actually {hero}.')
    print(f'{name} is actually {hero}')"""

    print(x)
    print(y)
    print(extra)
    print(result)

def trick_f():
    x = """  - A:
# Normal
items = (1, 2)
print(items)
# Output:
(1, 2)

"""
    y = """  - B:
# Unpacking
a, b = (1, 2)
print(a)
print(b)
# Output:
1
2
"""
    z = """  - C:
# Unpacking and skip with assign a underscore(_)
a, _ = (1, 2)
print(a)
# Output:
1
"""
    i = """  - D:
# Goto the memory address to get the rest of them.
a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
# Output:
1
2
[3, 4, 5]
"""
    j = """  - E:
a, b, *_, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(d)
# Output:
1
2
5"""
    print(x)
    print(y)
    print(z)
    print(i)
    print(j)

def trick_g():
    x = """  - A:
class Person():
    pass

person = person()
person.first = "Ron"
person.last = "Chang"

print(person.first)
print(person.last)

# Output:
Ron
Chang
"""
    y = """  - B:
class Person():
    pass

person = Person()
first_key = "first"
first_val = "Ron"
# person.first_key = first_val
# This is not what we need

setattr(person, first_key, first_val)
# setattr(obj, name, value)
first = getattr(person, first_key)
# getattr(object, name, default)
print(first)

# Output: Ron
"""
    i = """  - C:
class Person():
    pass

person = Person()
person_info = {"first": "Ron", "last": "Chang"}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

# Output:
Ron
Chang
"""

    j = """  - D:
class Person():
    pass

person = Person()
person_info = {"first": "Ron", "last": "Chang"}
for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

# Output:
Ron
Chang"""

    print(x)
    print(y)
    print(i)
    print(j)

def trick_h():
    x = """  - A:
username = input("Username: ")
password = input("Password: ")
print("Logging In...")
"""
    y = """  - B:
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
print("Logging In...")

# While you insert a password it wont show on the screen.
"""
    print(x)
    print(y)

def trick_i():
    x = """  - How:
# Edit [.zshrc] or [.bash_profile] insert information as
# export DB_USER="any_username"
# export DB_PASS="any_password"
# # No gap between equal sign

import os

username = os.environ.get("DB_USER")
password = os.environ.get("DB_PASS")
print(username)
print(password)
print("Logging In...")
"""
    link = "Tutorial: https://youtu.be/5iWhQWVXosU"

    print(x)
    print(link)

def trick_j():
    x = """  - How:
import numpy as np

# Check the full documentation
help(np) # hit "q" to extract

# Check avalible attributes
dir(np)
"""
    print(x)


def main():

    options = [str(i) for i in range(0,10+1)]
    functionTuple = (
                    extract,
                    trick_a,
                    trick_b,
                    trick_c,
                    trick_d,
                    trick_e,
                    trick_f,
                    trick_g,
                    trick_h,
                    trick_i,
                    trick_j,)

    while True:
        printInfo()

        usrinput = input(">>> ")

        if usrinput in options:
            print("-"*78)
            functionTuple[int(usrinput)]()

            print()
            pause = input("* Press [Enter] to continue...\r")
        else:
            print("\nInvalid Input!\n")






if __name__ == "__main__":
    main()


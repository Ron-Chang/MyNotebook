# Basel Problem

# Target

# input 3
# 1/9+1/4+1 == 1.3611111111

# input 10000000 == 1.6449339668472596

# input n -> ∞
# get 1/n^2 + 1/(n-1)^2 + ... + 1/3^2 + 1/2^2 + 1 == pi^2/6

# math.pi**2/6 == 1.6449340668482264


import sys
import math

def basel(num):

    result = 0

    for i in range(1,num+1):

        result += 1/i**2

    return result

if __name__ == "__main__":

    print("Input a integer.")
    while True:
        usrinput = input(">>> ")
        if usrinput.isdigit():
            if int(usrinput) != 0:
                break
            else:
                print("{} is invalid! Input a integer.".format(usrinput))
        else:
            print("{} is invalid! Input a integer.".format(usrinput))
            continue

    if int(usrinput) > 100000:
        print("\n")
        print("You input {} it gonna take a while.")

    a = basel(int(usrinput))
    print("\n")
    print("pi^2/6: {:.50f}".format(math.pi**2/6))
    print("result: {:.50f}".format(a))


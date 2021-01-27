import time

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
        # #equals
        # else:
        #     return True
def prime_nums():
    time_start = time.time()
    for i in range(2, 10000):
        if is_prime(i):
            print(i)
    time_end = time.time()
    duration = time_end - time_start
    print("In {:.4} s.".format(duration))

prime_nums()
"""logic with process function mix up together
kind of unreadable
"""

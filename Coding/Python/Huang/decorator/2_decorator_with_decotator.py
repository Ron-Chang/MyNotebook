import time

def timer(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        duration = time_end - time_start
        print("In {:.4} s.".format(duration))
    return wrapper

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
@timer
def prime_nums():
    for i in range(2, 40000):
        if is_prime(i):
            print("{:>6}".format(i))

prime_nums()
"""when we calling the function prime_nums(),
acctually we are calling the decorator timer().
we execute the function timer() which wrappes the function prime_nums()
"""

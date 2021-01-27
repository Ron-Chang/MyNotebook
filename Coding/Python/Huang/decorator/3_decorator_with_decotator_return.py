import time

def timer(func):
    def wrapper():
        time_start = time.time()
        result = func() #KEY: store the return from count_prime_nums()
        time_end = time.time()
        duration = time_end - time_start
        print("In {:.4} s.".format(duration))
        return result
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
def count_prime_nums():
    count = 0
    for i in range(2, 10000):
        if is_prime(i):
            count += 1
    return count
count = count_prime_nums()
print("{} Prime Numbers in 2 to 10000".format(count))
"""store count_prime_nums()'s return
into
timer().wrapper().result
then, return result
"""

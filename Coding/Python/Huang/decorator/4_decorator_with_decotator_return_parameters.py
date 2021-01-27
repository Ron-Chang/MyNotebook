import time

def timer(func):
    def wrapper(*args):
        time_start = time.time()
        result = func(*args) #KEY: store the return from count_prime_nums()
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
def count_prime_nums(maximum):
    count = 0
    for i in range(2, maximum):
        if is_prime(i):
            print(i)
            count += 1
    return count
count = count_prime_nums(10000)
print("{} Prime Numbers in 2 to 10000".format(count))
"""*args for unknown Numbers of parameter
execute line 33
put 10000 into line 27 as count_prime_nums(10000)
and follow the decorator @timer to execute the timer() function
then set up the time_start and execute the count_prime_nums(),
when it goes line 30, check Prime Numbers with the is_prime() function
when it has done return count back into the timer() and assign to the result
check the time with time_end,
get the time duration through by time_end minus time_start,
print duration time return result, return wrapper to the variable
which call the decorator function which is count in line 33.
print count
"""

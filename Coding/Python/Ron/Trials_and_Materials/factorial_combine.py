import time
"""
1!+2!+3!+4!+...+20!
"""
def f(n):
    results = []
    while n > 0:
        result=1
        for i in range(1,n+1):
            result*=i
        results.append(result)
        n-=1
    result = 0
    for i in results:
        result+=i
    return result

def g(n):
    if n == 1:
        return 1
    else:
        return n * g(n-1)

def h(n):
    result = 1
    # results = [i**i for i in range(1,n+1)]
    for i in range(1,n+1):
        result *= i
    return result

x = 100
# f method
t0 = time.time()
print(f(x))
t1 = time.time()
print(f"{t1-t0:.6f} SEC")
# g method
t2 = time.time()
print(sum([g(i) for i in range(1,x+1)]))
t3 = time.time()
print(f"{t3-t2:.6f} SEC")
# h method
t4 = time.time()
print(sum([h(i) for i in range(1,x+1)]))
t5 = time.time()
print(f"{t5-t4:.6f} SEC")

# # method 1 - For statement
def solveByFor(m):

    result = 0
    for i in range(1,m+1):
        if i%2 == 1:
            result += i
        else:
            result -= i
    return result

# method 2 - recursion with hints
def solveByRecursion_A(m):
    if m == 1:
        # print(f"m={m} and it supposed to be '1'")
        return 1
    else:
        if m%2 == 0:
            # print(f"m={m} which is even. change it to a negative number ({-m})")
            return(-m+solveByRecursion_A(m-1))
        else:
            # print(f"m={m} which is odd.")
            return(+m+solveByRecursion_A(m-1))

# # method 2 - recursion
def solveByRecursion_B(x):
    if x == 1:
        return 1
    else:
        if x%2 == 0:
            return(-x+solveByRecursion_B(x-1))
        else:
            return(+x+solveByRecursion_B(x-1))

# # method 3 - recursion with single if statement
def solveByRecursion_C(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return(-n+solveByRecursion_C(n-1))
    else:
        return(n+solveByRecursion_C(n-1))

# # method 4 - analyze the question
# # 1-2+3-4+5-6...+/-n
# # equivalent
# # (1-2)+(3-4)+(4-5)+(5-6)....+(n-(n+1))

def isEven(n):
    return True if n%2 == 0 else False

def solveByAnalyze_A(n):
    # pass
    if isEven(n):
        return int(-n/2)
    else:
        return n//2+1

# # method 5 - merge the function from methond 4
def solveByAnalyze_B(n):
    return int(-n/2) if n%2==0 else n//2+1

x = 101
answer = [  solveByFor(x),  # If x = 50_000_000 it took 5.7s
            solveByRecursion_A(x),  # RecursionError: maximum recursion depth exceeded in comparison
            solveByRecursion_B(x),  # maximum recursion depth = 1000
            solveByRecursion_C(x),  # sys.getrecursionlimit() or sys.setrecursionlimit(int)
            solveByAnalyze_A(x),  # If x = 50_000_000 it took 0.0s
            solveByAnalyze_B(x)]  # If x = 50_000_000 it took 0.0s

print(answer)


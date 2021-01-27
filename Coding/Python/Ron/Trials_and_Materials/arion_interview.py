"""
有兩種藥品，一共四顆，外觀無法辨識，早晚需要各服用一顆，服用錯誤或是不服用會死亡，
請問在混合的情況下要如何辨識服用呢？

各切一半，分成兩份服用
共：A+A+B+B = 2A+2B
早：A/2+A/2+B/2+B/2 == A+B
晚：A/2+A/2+B/2+B/2 == A+B
"""

"""
A = 5 Liter
B = 3 Liter
Get a 4 Liter by A and B container

Step 1:
A(5/5) -> B(0/3) = A(2/5) -> B(3/3)
Step 2:
B(3/3) -> Dump = B(0/3)
Step 3:
A(2/5) -> B(0/3) = A(0/5) -> B(2/3)
Step 4:
A(5/5) -> B(2/3) = A(4/5) -> B(3/3)

Container A == 4 is True
"""


"""
列出以下圖案
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
"""
def foo(x):

    i = 1

    while i < x:
        print(" "*int((x-i)/2) + "*"*i)
        i+=2

    while i >= 1:
        print(" "*int((x-i)/2) + "*"*i)
        i-=2

"""
計算1-2+3-4+5-6...+/-n
odd: 1,3,5,7 positive
even: 2,4,6,8 negaive
"""
def yoo(m):

    result = 0
    for i in range(1,m+1):
        if i%2 == 1:
            result += i
        else:
            result -= i
    return result

def zoo(m):
    if m == 1:
        print(f"m={m} and it supposed to be '1'")
        return 1
    else:
        if m%2 == 0:
            print(f"m={m} which is even. Changing to a negative number ({-m})")
            return(-m+zoo(m-1))
        else:
            print(f"m={m} which is odd.")
            return(+m+zoo(m-1))

divider = "-*"*20

print(divider)

x = 13
foo(x)

print(divider)

y = 3 # if y == 3, result == 2
loop_result = yoo(y)
print(f"Loop result: {loop_result}")

print(divider)

z = 3
recursive_result = zoo(z)
print(f"Recursive result: {recursive_result}")

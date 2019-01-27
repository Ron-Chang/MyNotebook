"""Format:
lambda arg1, arg2, ....: expression
"""

# Statement A

m = 3
n = 4
# This statement
x = m if m > n else n
# # equals:
# if m > n:
#     x = m
# else:
#     x = n

print(x)

# Statement B

# # This statement,
# def max(m, n):
#     if m > n:
#         result = m
#     else:
#         result = n
#     return result
# print(max(10, 3))

# # equals:
# def max(m, n):
#     return m if m > n else n
# print(max(10, 3))

# equals:
max = lambda m, n: m if m > n else n
print(max(10, 3))


# Simulate switch statement:
score = int(input('Input score ( 1-100 ): '))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()

"""Dict.get key method, if key not exsit return defult
{}.get(key,default=None)
"""

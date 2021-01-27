
# An example:
print("{0:.4f}->{0:.2f}\n{1:.4f}->{1:.2f}\n\n{2:.2f}->{2:.0f}\n{3:.2f}->{3:.0f}".format(123.445,123.446,123.400,123.500))

'''Result:
123.4450->123.44
123.4460->123.45

123.40->123
123.50->124
'''

a = round(1.115,2)
# 1.11
b = round(1.125,2)
# 1.13
print("{} == {} -> {}\n".format(a, b, a==b))

''' The reason is some float numbers cant stored exectly as binary numbers.
1.115，存儲為——1.1149999999999999911182158029987476766109466552734375
1.125，存儲為——1.125（可完全用二進制表示）

0.4，存儲為——0.40000000000000002220446049250313080847263336181640625
0.5，存儲為——0.5（可完全用二進制表示）
'''

# The easiest way to figure out
def round_up(value):
    # 替換內建round函數,實現保留2位小數的精確四捨五入
    return round(value * 100) / 100.0

print(round(1.115,2))
print(round_up(1.115))


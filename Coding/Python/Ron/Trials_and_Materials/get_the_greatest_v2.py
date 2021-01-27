# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using those digits, return -1:

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(n):
    origin = n
    data = str(n)
    data_dict = _convert_to_dict(data)

    result_str = str()
    for i in range(9, 0, -1):
        i_str = str(i)
        if i_str in data_dict:
            result_str += i_str*data_dict[i_str]

    if result_str:
        result = int(result_str)
        if result == origin:
            return -1
        else:
            return result

def _convert_to_dict(data):
    result = dict()
    for d in set(data):
        result.update({
            str(d):data.count(str(d))
            })
    return result

num = 9183433399
foo = next_bigger(num)
print(foo)

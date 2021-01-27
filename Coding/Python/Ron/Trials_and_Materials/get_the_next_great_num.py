# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If no bigger number can be composed using those digits, return -1:

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

import itertools

def is_greatest(data):
    ctns = dict()

    for d in set(data):
        ctns.update({
            str(d):data.count(str(d))
            })

    smallest = "".join([str(i)*ctns[str(i)] for i in range(10) if str(i) in ctns])
    greatest = smallest[::-1]

    if data == greatest:
        return True
    else:
        return False

def _possible_combinations_in_order(data):

    items = list()
    combinations = set(itertools.permutations(data))
    length = len(data)
    for i in combinations:
        item = "".join(i)
        items.append(int(item))
        items.sort()
    item_list = list()

    for item in items:
        item_str = str(item)
        if len(item_str) < length:
            item_list.append('0' + item_str)
        else:
            item_list.append(item_str)

    return item_list

def _get_bigger_by_index(num, combinations):

    index = combinations.index(num)
    if len(combinations) > index +1:
        return combinations[index+1]
    else:
        return num

def next_bigger(num):
    original = num
    num_str = str(num)
    length = len(num_str)
    switch_amount = 2

    if is_greatest(num_str):
        return -1

    while switch_amount <= length:

        part_A = num_str[:length-switch_amount]
        part_B = num_str[length-switch_amount:length]
        possible_list = _possible_combinations_in_order(part_B)
        bigger_one = _get_bigger_by_index(part_B, possible_list)
        new_one = str(part_A) + bigger_one

        if int(new_one) > original:
            return int(new_one)

        switch_amount+=1

    return -1

num = 998310
foo = next_bigger_2(num)
print(foo)

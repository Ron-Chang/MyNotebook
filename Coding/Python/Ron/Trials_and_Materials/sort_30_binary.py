"""
有一個數列，其包含30個二元數值:[
    0, 0, 0, 1, 0, 0, 0, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
    1, 0, 1, 1, 0, 0, 0, 1, 1, 1]

共兩個條件式：
-[條件 A]:
平分三組,
index [ 0]到[ 9] (0, 0, 0, 1, 0, 0, 0, 1, 1, 1)
index [10]到[19] (1, 1, 1, 1, 1, 1, 0, 1, 1, 1)
index [20]到[29] (1, 0, 1, 1, 0, 0, 0, 1, 1, 1)
任意兩組其奇數位值為1的項目大於3,則進行條件式B.

此數列,第一組false - 第二組true - 第三組true,
因此經過[條件Ａ]回傳true,繼續進行[條件B].

-[條件 B]:
不必分組,
任意奇數位數,若值為1其後緊接0回傳false.
index [ 0]到[ 9],
(0, 0, #true
0, 1, #true
0, 0, #true
0, 1, #true
1, 1) #true

index [10]到[19],
(1, 1, #true
1, 1, #true
1, 1, #true
0, 1, #true
1, 1) #true

index [20]到[29],
(1, 0, #false *
1, 1, #true
0, 0, #true
0, 1, #true
1, 1) #true

此數列經過[條件B],回傳false.

經過兩個條件後回傳false.
"""
import numpy as np

def solution_a(alist):

    array_1 = np.array(alist[0:10:2])
    array_2 = np.array(alist[10:20:2])
    array_3 = np.array(alist[20:30:2])

    array = array_1+array_2+array_3

    array2list = array.tolist()

    # check_list = [i for i in array2list if i > 1]
    check_list = []
    for i in array2list:
        if i >= 2:
            check_list.append(i)

    if len(check_list) >= 3:
        #分奇數組偶數組
        odd = [elemt for i,elemt in enumerate(alist) if i%2 == 0] #index == 0,2,4,6,8
        even = [elemt for i,elemt in enumerate(alist) if i%2 == 1] #index == 1,3,5,7,9

        for i,j in zip(odd, even):
            if i == 1 and j == 0:
                return False
        return True

    return False

def solution_b(alist):

    array = []
    for i,element in enumerate(alist,1):
        if i % 2 == 1:
            array.append(element)

    check_list = []

    if sum(array[0:5]) > 2:
        check_list.append("group_a is okay!")
    if sum(array[5:10]) > 2:
        check_list.append("group_b is okay!")
    if sum(array[10:15]) > 2:
        check_list.append("group_c is okay!")

    if len(check_list) >= 2:
        #分奇數組偶數組
        odd = [elemt for i,elemt in enumerate(alist) if i%2 == 0] #index == 0,2,4,6,8
        even = [elemt for i,elemt in enumerate(alist) if i%2 == 1] #index == 1,3,5,7,9

        for i,j in zip(odd, even):
            if i == 1 and j == 0:
                return False
        return True

    return False

alist = [  0, 0, 0, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
            1, 0, 1, 1, 0, 0, 0, 1, 1, 1]

result = solution_a(alist)

print(result)

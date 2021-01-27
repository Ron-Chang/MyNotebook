def merge_sort(ls):
    sub_sort(ls, 0, len(ls)-1)

def sub_sort(ls, first, last):
    if first < last:
        middle = (first + last) // 2
        sub_sort(ls, first, middle)
        merge_sort(ls, middle+1, last)
        merge(ls, first, middle, last)

def merge(ls, first, middle, last):
    L = ls[first:middle]
    R = ls[middle:last+1]
    L.append(999999999)
    R.append(999999999)

    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            ls[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j+=1


ls = [22,1,16,51,33,20,22]

def binary_sort(ls):

    length = len(ls)
    middle = length // 2

    ls_r = ls[:middle]
    ls_l = ls[middle:]

    result = list()
    if length == 1:
        print(ls)
        result.append(ls)
        return ls
    else:
        print(ls)
        binary_sort(ls_r)
        binary_sort(ls_l)



print(binary_sort(ls))

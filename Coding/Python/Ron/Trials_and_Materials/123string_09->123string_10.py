def increment_string(strng):
    if strng.isalpha() or strng == "":
        return strng + "1"
    elif strng.isdigit():
        num = str(int(strng)+1)
        return "0"*(len(strng)-len(num)) + num
    else:
        for index, s in enumerate(strng[::-1]):
            i = len(strng) - (index+1)
            # print(f"{i}: {index} - {s}")
            if s.isdigit():
                continue
            else:
                # "  *   "
                # "asd123"
                # "d" is including strng[i:]

                # print(f"{i}: {index} - {s}")
                num = str(int(strng[i+1:])+1)

                if len(num) == len(strng[i+1:]):
                    return strng[:i+1] + num
                else:
                    return strng[:i+1] + "0"*(len(strng[i+1:])-len(num)) + num

"""clever way
def increment_string(strng):
    # 取頭 : 去掉右邊所有包含(0-9的數字)
    head = strng.rstrip('0123456789')
    # 取尾 ; 透過head的長度切片取得尾
    tail = strng[len(head):]
    如果字尾為空（純文字或是無文字）直接補 "1" ，回傳
    if tail == "": return strng+"1"

    頭 加 尾(數字+1(透過zfill補齊0(尾的長度)) ，回傳
    return head + str(int(tail) + 1).zfill(len(tail))
    # txt = "13xz"
    # print(txt.zfill(10)) # resutl: 00000013xz
"""
txt = "13xz"
print(txt.zfill(10))
print(increment_string('893822851#`/09'))

def odd():
    return [i for i in range(1,100)[::2]]
    # return "->".join(str(i) for i in range(1,100)[::2])

def even():
    return [i for i in range(100)[::2]]


if __name__ == "__main__":
    while True:
        usrinput = input("1. Odd.\t2. Even.\nInput(1-2): ")
        if usrinput == '1':
            print("1. 1-99 odd numbers:\n")
            print("def odd():")
            print("\treturn [i for i in range(1,100)[::2]]\n\n")
            print(odd())
            print("\n\n\n")

        elif usrinput == '2':
            print("2. 1-99 even numbers:\n")
            print("def even:\n")
            print("\treturn [i for i in range(100)[::2]]\n\n")
            print(even())
            print("\n\n\n")

        else:
            print("+"+"-"*25+"+")
            print("|      Invalid Input      |")
            print("| Function is Terminated! |")
            print("+"+"-"*25+"+")
            quit()


# s = 'abcdefg'
# # 返回從起始位置到索引位置 2 處的字符串切片
# print(s[:3]) # 輸出 'abc'

# # 返回從第三個索引位置到結尾的字符串切片
# print(s[3:]) # 輸出 'defg'

# # 字符串反向輸出
# print(s[::-1]) # 輸出 'gfedcba'

# # 輸出從開始位置間隔一個字符組成的字符串
# print(s[::2]) # 輸出 'aceg'
# print(range(10)[::2])  # 輸出偶數：[0, 2, 4, 6, 8]

# # 它們也可以相互結合使用。
# # 從索引位置 6 到索引位置 2，反向間隔一個字符
# print(s[6:2:-2]) # 輸出'ge'

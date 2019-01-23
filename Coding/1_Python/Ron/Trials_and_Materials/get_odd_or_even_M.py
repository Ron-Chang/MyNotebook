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
# # 返回从起始位置到索引位置 2 处的字符串切片
# print(s[:3]) # 输出 'abc'

# # 返回从第三个索引位置到结尾的字符串切片
# print(s[3:]) # 输出 'defg'

# # 字符串逆序输出
# print(s[::-1]) # 输出 'gfedcba'

# # 输出从开始位置间隔一个字符组成的字符串
# print(s[::2]) # 输出 'aceg'
# print(range(10)[::2])  # 输出偶数：[0, 2, 4, 6, 8]

# # 它们也可以相互结合使用。
# # 从索引位置 6 到索引位置 2，逆向间隔一个字符
# print(s[6:2:-2]) # 输出'ge'

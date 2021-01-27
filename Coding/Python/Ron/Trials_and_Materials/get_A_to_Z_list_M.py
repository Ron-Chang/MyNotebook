def list_A_Z_1():

    A_Z_list = []
    for i in range(ord('A'),ord('Z')+1):
        A_Z_list.append(chr(i))

    return A_Z_list


def list_A_Z_2():
    '''
    [i for i in range(a,b) if i > x]
    i == variable to process and store
    This statement quals:

    list = []
    for i in range(a,b):
        if i > x:
            list.append(i)
    '''

    # Double = [str(i)+'*'+str(j)+'='+str(i*j) for i in range(2,10) if i%2 == 0 for j in range(2,10) if j%2 == 0]

    return [chr(i) for i in range(ord('A'),ord('Z')+1)]


if __name__ == "__main__":
    while True:
        usrinput = input("1. Basic Way.\t2. Advance Way.\nInput(1-2): ")
        if usrinput == '1':
            print("1. Basic way:\n")
            print("def list_A_Z_1():")
            print("\tA_Z_list = []")
            print("\tfor i in range(ord('A'),ord('Z')+1):")
            print("\t\tA_Z_list.append(chr(i))")
            print("\nreturn A_Z_list")
            print("\n\n\n")
            print(list_A_Z_1())
            print("\n\n\n")

        elif usrinput == '2':
            print("2. Advance way:\n")
            print("def list_A_Z_2():\n")
            print("\treturn [chr(i) for i in range(ord('A'),ord('Z')+1)]")
            print("\n\n\n")
            print(list_A_Z_2())
            print("\n\n\n")

        else:
            quit("You Enter something else, \nFunction Terminated! ")

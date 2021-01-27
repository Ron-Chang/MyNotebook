import random
import sys
import time
def generator(method, numbers,col=5):
    li = [chr(random.randint(65,90+1)) for i in range(0,numbers)]
    info = f"[All the elements for method:{method}"
    left_space = int((col*4-len(info))/2)
    sys.stdout.write(" "*left_space + f"{info}")
    sys.stdout.flush()
    for i, elemt in enumerate(li):
        if i%col == 0:
            sys.stdout.write(f"]")
            print()
            sys.stdout.write(f"[")
            sys.stdout.write(f"{elemt:>3},")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"{elemt:>3},")
            sys.stdout.flush()
    print("]\n")

    return li

def normalGet(li):
    # 遇重複最多項，無法提取
    # ISSUE: Cannot sovle a multiple greatest container.

    items = []
    item_nums = []

    while len(li) > 0:

        item = li[0]
        item_num = li.count(item)
        print(f"{item:^3}有{item_num:>3} 個")
        items.append(item)
        item_nums.append(item_num)
        while item in li:
            li.remove(item)

    index = item_nums.index(max(item_nums))
    return item_nums[index], items[index]



def sort_n_get(li):

    # Get the targets length
    vol = len(li)

    # remove the same items through set()
    catalog = set(li)

    # create containers
    dic={}
    keys = []
    values = []
    results = []

    # count with catalog
    for key in catalog:
        dic[key]=li.count(key)

    # Descending check from vol which is the total.
    for num in range(vol, 0, -1):
        for key in dic.keys():
            if dic[key] == num:
                print(f"{key:^3}有{num:>3} 個")
                keys.append(key)
                values.append(num)

    # check is there any number is the same
    i = 1
    while True:
        try:
            if values[i] == values[i-1]:
                results.append(keys[i-1])
            else:
                results.append(keys[i-1])
                break
            i+=1
        except:
            even_info = "All elements are the same quantity."
            results = f"{even_info} which is \n{li}"
            break

    return values[i-1],results

if __name__ == "__main__":
    quantity = 20_000
    # It won't be a such different when the quantity under 250.
    li = generator(1,quantity,10)
    t0 = time.time()
    results_1 = normalGet(li)
    t1 = time.time()

    divider = " divider "
    print(f"{divider:*^50s}")

    li = generator(2,quantity,10)
    t2 = time.time()
    results_2 = sort_n_get(li)
    t3 = time.time()

    time_1 = t1-t0
    time_2 = t3-t2
    print(f"{divider:*^50s}")
    print(f"    Quantity: {quantity:,}")
    print(f"There are {results_1[0]} '{results_1[1]}' which is the greatest number")
    print(f"    Method_01: {time_1:.6f}")
    print(f"There are {results_2[0]} {results_2[1]} which is the greatest number")
    print(f"    Method_02: {time_2:.6f}")

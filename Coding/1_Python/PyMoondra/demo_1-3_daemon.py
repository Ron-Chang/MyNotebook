# daemon屬性，預設為false
# 當主執行緒結束，用來停止其他執行緒

import threading
import time

total = 4

def create_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')

def create_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')

def limit_items():

    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted 3')

        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target = create_items)
creator2 = threading.Thread(target = create_items_2)
limitor = threading.Thread(target = limit_items, daemon = True)
# Once our main thread is finishing, the background thread will be terminate

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()
# limitor.join()  # 1不會結束

# limitor.daemon()
print(f'THE VALUE IS ENDING WITH {total}')

# lock 變數上鎖, lock variabl
# 應用在多線程執行時有機會存取同一變數
# apply to multi-thread which might access or share the same variable
# we can lock it until the processing tread has finished
import threading

# def adding_2():
#     global x
#     lock.acquire()
#     for i in range(COUNT):
#         x += 2
#     lock.release()

# #  equivalent the following function

def adding_2():
    global x
    with lock:
        for i in range(COUNT):
            x += 2

def adding_3():
    global x
    with lock:
        for i in range(COUNT):
            x += 3

def subtracting_4():
    global x
    with lock:
        for i in range(COUNT):
            x -= 4

def subtracting_1():
    global x
    with lock:
        for i in range(COUNT):
            x -= 1

if __name__ == '__main__':

    x = 0
    COUNT = 100000
    lock = threading.Lock()

    t1 = threading.Thread(target=adding_2, name='thread_add_2')
    t2 = threading.Thread(target=subtracting_4, name='thread_sub_4')
    t3 = threading.Thread(target=adding_3, name='thread_add_3')
    t4 = threading.Thread(target=subtracting_1, name='thread_sub_1')
    # x = 0+2-4+3-1 = 0

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(x)


# queue 排隊, lock variabl

# utilize, manipulate


# 應用在多線程執行時有機會存取同一變數
# Basically is a container of data item slash command to retreat
# for instance,
# Receive the data from a website, and it's going to be writing to a file.
# You can't manipulate the data if you haven't receive it yet.
# You don't wanna save the data if you haven't modidied it yet.

# FIFO - first in first out
# LIFO - last in first out
# Priority

import queue

q = queue.Queue()

# # single put item to queue, get it and check queue is empty
# q.put(5)
# print(q.get())
# print(q.empty())

# # multiple put and get by check queue is empty
# for i in range(5):
#     q.put(i)

# while not q.empty():
#     print(q.get(), end = ' || ')


# # if we get over the amount of queue, the program will be freezed
# q.put(5)

# print(q.get())
# print('first item gotten')

# print(q.get())
# print('finished')


# overcome the previous problem
import threading
import time

def putting_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')

q = queue.Queue()
t = threading.Thread(target = putting_thread, args = (q, ), daemon = True)
t.start()

q.put(5)

print(q.get())
print('first item gotten')

print(q.get())
print('finished')









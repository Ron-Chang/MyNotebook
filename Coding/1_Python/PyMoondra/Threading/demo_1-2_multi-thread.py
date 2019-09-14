# 示範 多執行緒 multi-thread

import threading
import time

def sleeper(n, name):
    print(f"Hi, I am {name}. Going to sleep for {n} sec")
    time.sleep(n)
    print(f"{name} has woken up from sleep")

threads_list = list()

start = time.time()
for i in range(5):
    t = threading.Thread(target = sleeper, name = f'thread{i}', args = (2, f'thread_{i}'))
    threads_list.append(t)
    t.start()
    print(f'{t.name} has started')

for t in threads_list:
    t.join()
    # 阻塞主執行緒執行
print(f' CONSUME: {time.time()-start} sec.')
print('All threads have finished their jobs .')

############################## without multiple threading #############################################
start = time.time()
for i in range(5):
    print(f'Iteration {i} has started')
    sleeper(2, i)
print(f' CONSUME: {time.time()-start} sec.')
#######################################################################################################

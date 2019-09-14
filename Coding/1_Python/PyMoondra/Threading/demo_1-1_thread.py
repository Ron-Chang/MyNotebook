# 示範 執行緒

import threading
import time

def sleeper(n, name):
    print(f"Hi, I am {name}. Going to sleep for {n} sec\n")
    time.sleep(n)
    print(f"{name} has woken up from sleep")

t = threading.Thread(target = sleeper, name = 'thread1', args = (5, 'thread_1'))
# 實例化module，使用 Thread方法，
# target 指定要執行的函數
# name 該執行緒的名稱
# args 為賦予函數使用的參數

t.start()
# 啟動該執行緒
t.join()
# 阻塞，避免主程序在執行緒處理完成前偷跑

print('Hello')
print('Hello')
# 即便 sleeper 沒有執行完成，兩次 Hello 會先被打印

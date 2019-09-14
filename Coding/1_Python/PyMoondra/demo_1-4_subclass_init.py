import time
import threading

class MyThread(threading.Thread):

    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        start = time.time()
        print(f'thread {self.number} has started.')
        self.func(*self.args)
        print(f'thread {self.number} has finished.')
        print(f'CONSUME: {time.time()-start} sec.')

def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)

threads_list = list()

for i in range(50):
    t = MyThread(number = i+1, func = double, args = [i, 15])
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()

print('DONE!')

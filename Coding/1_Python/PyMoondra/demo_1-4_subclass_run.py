import time
import threading

class MyThread(threading.Thread):

    def run(self):
        start = time.time()
        print(f'{self.getName()} has started!')

        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

        print(f'{self.getName()} has finished!')
        print(f'CONSUME: {time.time()-start} sec.')

def sleeper(n, name):
    print(f"Hi, I am {name}. Going to sleep for {n} sec\n")
    time.sleep(n)
    print(f"{name} has woken up from sleep")


for i in range(4):
    t = MyThread(target = sleeper, name = f'THREAD-{i}', args = (3, f'thread[{i}]'))
    t.start()


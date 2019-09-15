# SUPER 繼承

import time
import threading
import sys as _sys
from threading import current_thread, _newname, Event

class MyThread(threading.Thread):

    def __init__(self, group=None, target=None,
                name=None, args=(), kwargs=None, *,
                daemon=None, number, style):

        assert group is None, "group argument must be None for now"
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._name = str(name or _newname())
        self._args = args
        self._kwargs = kwargs
        if daemon is not None:
            self._daemonic = daemon
        else:
            self._daemonic = current_thread().daemon
        self._ident = None
        self._tstate_lock = None
        self._started = Event()
        self._is_stopped = False
        self._initialized = True

        self._stderr = _sys.stderr

        self.number = number
        self.style = style


    def run(self):

        print('A_thread starting')
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print('A_thread has ended')

####################################### 等價於 #######################################

    def __init__(self, number, style, *args, **kwargs):

        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print('B_thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('B_thread has ended')


def sleeper(num, style):
    print(f'we are sleeping for {num} seconds as {style}.')
    time.sleep(num)
    # print(f"{style} has woken up from sleep")

t = MyThread(number = 3, style = 'yellow', target = sleeper, args = [3, 'yellow'])
t.start()

# for i in range(4):
#     t = MyThread(target = sleeper,number = 3, style = f'THREAD-{i}', args = (3, f'thread[{i}]'))
#     t.start()


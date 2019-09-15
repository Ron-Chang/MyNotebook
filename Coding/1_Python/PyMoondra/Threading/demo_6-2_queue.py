# FIFO, LIFO and Priority QUEUE

import queue
import time

############ FIFO QUEUE ############
fifo_q = queue.Queue()

for i in range(5):
    fifo_q.put(i)

while not fifo_q.empty():
    print(f'| {fifo_q.get()} |', end="")

# RESULT: | 0 || 1 || 2 || 3 || 4 |

print('\n','#'*24)

############ LIFO QUEUE ############
lifo_q = queue.LifoQueue()

for i in range(5):
    lifo_q.put(i)

while not lifo_q.empty():
    print(f'| {lifo_q.get()} |', end="")

# RESULT: | 4 || 3 || 2 || 1 || 0 |

print('\n','#'*24)

############ Priority QUEUE ############
# lowest number will be pulled out firsr
priority_q = queue.PriorityQueue()

priority_q.put((1, 'RON'))
priority_q.put((3, 'CHANG'))
priority_q.put((0, 'MIKE'))
priority_q.put((4, 'JACK'))
priority_q.put((2, 'LEE'))
for i in range(priority_q.qsize()):
    print(f'| {priority_q.get()[1]} |', end="")

# RESULT: | 0 || 1 || 2 || 3 || 4 |

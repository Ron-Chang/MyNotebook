from progressbar import *

x = [chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]

maxmun = len(x)

bar = ShowProcess(maxmun, 'OK')



for i in range(maxmun):
    bar.show_process()
    time.sleep(0.01)
'''

max_steps = 100

process_bar = ShowProcess(max_steps, 'OK')

for i in range(max_steps):
    process_bar.show_process()
    time.sleep(0.01)
'''

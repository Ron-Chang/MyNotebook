import time
import sys

"""
Check:
https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
"""

print("sample 01")
for i in range(5):
    print(i)
    time.sleep(1)

print("sample 02")
for i in range(5):
    print(i)
    sys.stdout.flush()
    time.sleep(1)


print("sample 03")
for i in range(10):
    print(i)
    if i == 5:
        print("Flushing buffer")
        sys.stdout.flush()
    time.sleep(1)

for i in range(10):
    print(i)
    if i == 5:
        print("Flushing buffer")
        sys.stdout.flush()

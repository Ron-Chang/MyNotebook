# # ########################## single thread version ##########################

# # import os
# # import requests
# # import time

# def download_img(save_dir, img_links, session = None):

#     if not session:
#         session = requests.Session()
#     for num, link in enumerate(img_links):
#         try:
#             r = session.get(link)
#         except (requests.exceptions.RequestException, UnicodeError) as err:
#             print("="*30, err)

#         print('image', num)
#         with open(os.path.join(save_dir, f'image_{num}.jpg'), 'wb') as f:
#             f.write(r.content)

# save_dir = r'/Users/ron/Downloads/thread_download_exam/'
# img_links = list()
# count = 0

# with open(r'links.txt', 'rt') as f:
#     for i in range(40):
#         line = f.readline()
#         img_links.append(line.strip())
#         count += 1

# print(f'download img amount: {len(img_links)}')

# start = time.time()
# download_img(save_dir, img_links)
# print(f'CONSUME : {time.time()-start:.4f} sec.')
# # download 40 imgs CONSUME : 26.0202 sec.


########################## multiple thread version ##########################

import os
import requests
import time
import queue
from threading import Thread, Lock

save_dir = r'/Users/ron/Downloads/thread_download_exam/'

img_count = 0

def download_img(save_dir, q, session = None):
    global img_count
    if not session:
        session = requests.Session()

    while not q.empty():

        try:
            r = session.get(q.get(block = False))

        except (requests.exceptions.RequestException, UnicodeError) as err:
            print("="*30, err)
            img_count += 1
            q.task_done()
            continue

        img_count += 1
        q.task_done()

        print(f'image {img_count}')
        with open(os.path.join(save_dir, f'image_{img_count}.jpg'), 'wb') as f:
            f.write(r.content)

q = queue.Queue()
with open(r'links.txt', 'rt') as f:
    for i in range(40):
        line = f.readline()
        q.put(line.strip())  # To prevent space and empty line
print(f'queue amount: {q.qsize()}')

threads = list()

start = time.time()
for i in range(20):
    t = Thread(target = download_img, args = (save_dir, q))
    threads.append(t)
    t.start()
q.join()

for t in threads:
    t.join()

print(f'CONSUME : {time.time()-start:.4f} sec.')
# download 40 imgs CONSUME : 1.9717 sec.

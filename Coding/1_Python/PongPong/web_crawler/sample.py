"""Sample 1 Error
import urllib.request as req

url = "https://store.steampowered.com/search/?specials=1"

with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)
"""


"""Sample 1 Access to get the page
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
# Create a Request Object, and attached Request Headers information
request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    })

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)
"""

import urllib.request as req
import bs4

url = "https://www.ptt.cc/bbs/movie/index.html"
# Create a Request Object, and attached Request Headers information
request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    })

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root=bs4.BeautifulSoup(data, "html.parser")
"""
print(root.title.string)
"""
"""
# find the first class = "title" tag of div tag
title=root.find("div",class_="title")
print(title.a.string)
"""
# find all the class = "title" tag of div tag
titles=root.find_all("div",class_="title")
for title in titles:
    # If title link is exist, then print
    if title.a != None:
        print(title.a.string)

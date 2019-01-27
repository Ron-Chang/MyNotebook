import urllib.request as req
import bs4
import time


# Create a Request Object, and attached Request Headers information
# request=req.Request(url, headers={
#         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
#     })

pages = input("How many pages you would like to crawler? ")

t1 = time.time()

for page in range(1,int(pages)+1):
    main_address = "https://store.steampowered.com"
    side_address = "/search/?specials=1&page="
    # url = main_address + side_address + str(page)
    url = "file:///Users/ron/Downloads/Steam%20Search.html"
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")

    titles=root.find_all("span",class_="title")

    for title in titles:
        print (title.string)
        # if  "'s" in title.string:
        #     print((title.string).replace("'s"," is"))

        # else:
        #     print(title.string)

t2 = time.time()

print("\n\n"+"-"*20)
print ("Crawler {} pages for {:.3f} s".format(pages,t2-t1))

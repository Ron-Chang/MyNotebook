from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import chdir,getcwd,makedirs
from progressbar import *

# Opening up connection, grabbing the page
# my_url = "file:///Users/ron/Documents/MyNotebook/Coding/1_Python/PongPong/web_crawler/steam_promotion.html"
try:
    chdir("data")
except:
    makedirs("data")
    chdir("data")
url = "https://store.steampowered.com/search/?os=win&specials=1&page="
pages = input("How many pages you would like to crawler? ")
#Opening and Writing header into the file
filename = "steam_scrape.csv"
file = open(filename, "w")
header = "Name, Discount, Original_Price, Sale_Price, Review, Review_info \n"
file.write(header)
file.close()

#Progress Bar
maxmun = int(pages)+1
bar = ShowProcess(maxmun, 'Done!')

for page in range(1,int(pages)+1):
    my_url = url + str(page)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    file = open(filename, "a")

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs each product
    containers = page_soup.findAll("a",{"class":"search_result_row ds_collapse_flag"})

    bar.show_process()
    time.sleep(0.01)

    for container in containers:
        name = container.span.string
        img = container.img["src"]

        review_container = container.findAll("div",{"class":"col search_reviewscore responsive_secondrow"})
        # review = review_container[0].span["data-tooltip-html"]
        if review_container[0].span == None:
            review = ["None","None"]
        else:
            review = review_container[0].span["data-tooltip-html"].replace("<br>","\n").replace(" for ","\n").replace(",","_").split("\n")

        discount_container = container.findAll("div",{"class":"col search_discount responsive_secondrow"})
        discount = discount_container[0].span.text.strip("-")

        price_container = container.findAll("div",{"class":"col search_price discounted responsive_secondrow"})
        original_price = price_container[0].span.string
        sale_price = price_container[0].text.replace(price_container[0].span.string,"").strip()
        all_info = (name + ", " + discount + " OFF" + ", " + original_price + ", " + sale_price + "," + review[0] + "," + review[1] + "\n")

        # print("Name: {} [{} off]\nPrice: {} -> {}\n{}\n{}\n".format(name, discount, original_price, sale_price, review[0], review[1]))
        file.write(all_info)

file.close()
print("-"*80)
print("Data has been Saved\nDirectory: '{}/stream_scrape.csv'".format(getcwd()))

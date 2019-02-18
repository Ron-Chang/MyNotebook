from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import chdir,getcwd

# Opening up connection, grabbing the page
# my_url = "file:///Users/ron/Documents/MyNotebook/Coding/1_Python/PongPong/web_crawler/steam_promotion.html"

url = "https://store.steampowered.com/search/?os=win&specials=1&page="
page = "10"
my_url = url + page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Opening and Writing header into the file
chdir("data")
filename = "steam_scrape.csv"
file = open(filename, "w")
header = "Name, Discount, Original_Price, Sale_Price, Review, Review_info \n"
file.write(header)

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("a",{"class":"search_result_row ds_collapse_flag"})

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
    if discount_container[0].span  == None:
        discount = "0%"
    else:
        discount = discount_container[0].span.text.strip("-")

    price_container = container.findAll("div",{"class":"col search_price discounted responsive_secondrow"})
    if price_container != []:
        original_price = price_container[0].span.string
        sale_price = price_container[0].text.replace(price_container[0].span.string,"").strip()
    else:
        price = container.findAll("div",{"class":"col search_price responsive_secondrow"})
        original_price = price[0].string.strip()
        sale_price = "None"

    all_info = (name + ", " + discount + " OFF" + ", " + original_price + ", " + sale_price + "," + review[0] + "," + review[1] + "\n")
    print("Name: {} [{} off]\nPrice: {} -> {}\n{}\n{}\n".format(name, discount, original_price, sale_price, review[0], review[1]))
    file.write(all_info)

file.close()
print("-"*80)
print("Data has been Saved as:'{}/stream_scrape.csv'".format(getcwd()))

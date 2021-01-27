# Python 網路連線程式、公開資料串接  
<p align="right""> by <a href="https://youtu.be/9Z9xKWfNo7k/">Jake Wright</a></p>  


1. 抓取特定網址的資料
1.1 觀察想要抓取的網頁，取得網址
1.2 利用開發人員工具，觀察網路連線細節 (Request Headers)
1.3 建立 Request 物件，附加 Request Headers 設定。

2. 解析 HTML 格式資料
2.1 認識 PIP 套件管理工具
2.2 利用 PIP 安裝第三方套件 BeautifulSoup
2.3 利用 BeautifulSoup 解析並取得資料

3. 實務操作：抓取 PTT 電影版的文章標題

Sample:
```python
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)
```
>result:
...
...
urllib.error.HTTPError: HTTP Error 403: Forbidden

Most webpage refuse directly get data, we have to acting like a normal user  

use website developtool inspect the page.
`Network` `All` refresh the page, hit `index.html`, check 'headers'.
Found `user-agent:` in `Request Headers`
 
Final
```python
import urllib.request as request
import json

link_1 = "https://data.taipei/opendata/datalist/apiAccess?scope="
link_2 = "resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
src=link_1+link_2

with request.urlopen(src) as response:
    data=json.load(response)
    # load and process by json mod


data_enlist = data["result"]["results"]

for company in data_enlist:
    print(company["公司名稱"])

with open("company_name.txt", "w", encoding="utf-8") as file:
    for company in data_enlist:
        file.write(company["公司名稱"]+"\n")
```

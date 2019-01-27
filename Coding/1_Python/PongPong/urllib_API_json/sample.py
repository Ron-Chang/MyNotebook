"""Sample 1
import urllib.request as request

src="http://www.ntu.edu.tw/"

with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
    # Get data from NTU
print(data)
"""

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

with open("company_nmae.txt", "w", encoding="utf-8") as file:
    for company in data_enlist:
        file.write(company["公司名稱"]+"\n")

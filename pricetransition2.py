from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


year = []
name = []
for page in range(2015,2019):
        url = "https://aucfree.com/search?c=2084055844&from=" + str(page) + "-07&o=t2&q=マルスゾウカブト&to=" + str(page) + "-07"
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")

        for i in soup.find_all("div", id="bid_search_tittle"):
                year.append(i.string)
        for o in soup.find_all("strong", id="mean_price"):
                name.append(o.string)


df = pd.DataFrame({"name":name, "year":year})

print(df)
df.to_csv("tosho1_fake.csv", header=False, index=False)
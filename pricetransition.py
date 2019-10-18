import requests
from bs4 import BeautifulSoup
import csv


def generaterUrl(year, month):
    return (f"https://aucfree.com/search?c=2084055844&from={year}-{month}&o=t2&q=%E3%83%9E%E3%83%AB%E3%82%B9%E3%82%BE%E3%82%A6%E3%82%AB%E3%83%96%E3%83%88&to={year}-{month}")
  
csvlist = [["","2015-2019 マルスゾウカブトの出品価格"]]
num = 1
#for文で2015年~2019年まで回す。
for year in range(2015,2020):
    
        for month in range(1,13):
                base_url = generaterUrl(year, month)
                r = requests.get(base_url)
                r.encoding = r.apparent_encoding
                soup = BeautifulSoup(r.text,'lxml')
                items = soup.findAll('td',class_='results-price')
                
                for prices in items:

                        for price in prices.findAll('a',class_='item_price'):
                                p = price.getText()
                                csvlist.append([num,year,month,p])
                                num += 1


                                                        
                # CSVファイルを開く。ファイルがなければ新規作成する。
with open('output.csv', 'w') as f:
        writecsv = csv.writer(f)
        writecsv.writerows(csvlist)



            
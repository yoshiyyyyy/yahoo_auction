import requests
from bs4 import BeautifulSoup
import csv


def generaterUrl(year, month):
    return (f"https://aucfree.com/search?c=2084055844&from={year}-{month}&o=t2&q=%E3%83%9E%E3%83%AB%E3%82%B9%E3%82%BE%E3%82%A6%E3%82%AB%E3%83%96%E3%83%88&to={year}-{month}")

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
  
csvlist = [["2015-2019 マルスゾウカブトの出品価格"] ]

#for文で2015年1月~2019年12月まで回す。
for year in range(2015,2020):

        for month in range(1,13):

                if month <= 9:
                        month = str(0) + str(month)
                        base_url = generaterUrl(year, month)
                        r = requests.get(base_url,headers=headers)
                        r.encoding = r.apparent_encoding
                        soup = BeautifulSoup(r.text,'lxml')
                        print(soup)
                        items = soup.findAll('tr',class_='avg')

                else:
                        base_url = generaterUrl(year, month)
                        r = requests.get(base_url)
                        r.encoding = r.apparent_encoding
                        soup = BeautifulSoup(r.text,'lxml')
                        items = soup.findAll('tr',class_='avg')
                        
                for prices in items:

                        for price in prices.findAll('strong'):
                              
                                p = price.getText()
                                csvlist.append([str(year) + "." + str(month) + "," +str(p)])

                                         
                # CSVファイルを開く。ファイルがなければ新規作成する。
with open('output.csv', 'w') as f:
        writecsv = csv.writer(f)
        writecsv.writerows(csvlist)



            
import requests
from bs4 import BeautifulSoup
import csv
import time



def GenerateUrl(year, month):
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     aucfreeで調べたい商品のカテゴリと名前を指定して検索。その時のURLを以下にコピペ。URLで"{~年}"と"{~月}"だった部分は以下のように"{year}"と"{month}"にしてください。
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return (f"https://aucfree.com/search?c=20840242343224242&from={year}-{month}&o=t2&q=%E3%82%A4%E3%83%B3%E3%82%AB%E3%83%84%E3%83%8E%E3%82%B3%E3%82%AC%E3%85&to={year}-{month}")
    

def FetchMeanPrice(year,month):
        base_url = GenerateUrl(year, month)
        r = requests.get(base_url,headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'lxml')
        return soup


headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
csvlist = [['落札年月日','月内平均価格','落札価格','商品名']]

#----------------------------------------------------------------------------------------------------
#rangeには調べたい期間を適宜入れてください。以下は2015年1月~2020年12月のデータを対象にします。
#----------------------------------------------------------------------------------------------------
for year in range(2015,2021):
        for month in range(1,13):
                if month <= 9:
                        month = str(0) + str(month)
                        soup = FetchMeanPrice(year,month)
                        #--------------------------------------------------
                        #sleepは5秒以上だとアク禁されたことは有りません。
                        #--------------------------------------------------
                        time.sleep(5)
                        mean_price = soup.findAll('strong',id='mean_price')
                        item_title = soup.findAll('a',class_='item_title')
                        item_price = soup.findAll('a',class_='item_price')
                else:
                        soup = FetchMeanPrice(year,month)
                        mean_price = soup.findAll('strong',id='mean_price')
                        item_title = soup.findAll('a',class_='item_title')
                        item_price = soup.findAll('a',class_='item_price')
                for i in mean_price:
                        i = i.text.replace(',','')
                        #    .textでタグ型オブジェクトからテキストを取り出す
                        if int(i) == 0:
                            continue
                        else:
                            for k,l in zip(item_title,item_price):
                                k = k.text.replace(',','')
                                l = l.get_text().replace(',', '').replace('円', '')

                                csvlist.append([int(str(year)+str(month)),int(i),int(l),k]) 

#---------------------------------------------              
#.csvの前は任意のファイル名指定してください         
# ---------------------------------------------                               
with open('sample.csv', 'w') as f:
        writecsv = csv.writer(f)
        writecsv.writerows(csvlist)
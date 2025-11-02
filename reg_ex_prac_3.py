import urllib.request
import re

url = "https://finance.naver.com/item/main.naver?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf8"))

stock_result = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_result[0]
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
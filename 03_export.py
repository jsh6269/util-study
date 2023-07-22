import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://finance.naver.com/"
response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")
name = data.select("#container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr > th > a")
d1 = data.select("#container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr > td:nth-child(2)")
d2 = data.select("#container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr > td:nth-child(3) > em > span")
d3 = data.select("#container > div.aside > div > div.aside_area.aside_stock > table > tbody > tr > td:nth-child(3)")

dataList = []
for i in range(len(name)):
    x = name[i].get_text().strip()
    y = d1[i].get_text().strip()
    arrow = '△ ' if d2[i].get_text().strip() == "상승" else '▽ '
    z = arrow + d3[i].get_text().strip().split(' ')[1]
    print(x, y, z)
    dataList.append([x, y, z])

wb = Workbook()
write_ws = wb.create_sheet('Stock')
wb.remove(wb['Sheet'])
for data in dataList:
    write_ws.append(data)

wb.save('sample/Stock.xlsx')

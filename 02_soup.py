import requests
from bs4 import BeautifulSoup

# '다시금' 검색 url
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EB%8B%A4%EC%8B%9C%EA%B8%88"
response = requests.get(url)

if response.status_code == 200:
    htmlText = response.text
    soupData = BeautifulSoup(htmlText, "html.parser")
    # 기사 제목 선택자로 추출
    headline = soupData.select('#container > li > div.wrap_cont > a')
    headlines = [headline[i].getText() for i in range(len(headline))]
    for title in headlines:
        print(title)

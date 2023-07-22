import requests
url = "http://bitly.ws/M7e4"
response = requests.get(url)

# 200: 정상적으로 처리됨
print(response.status_code)
# response.text로 html을 받아올 수 있음
htmlText = response.text
print(htmlText.strip()[:250], '\n')

searchNum = htmlText.count('다시금')
print("다시금은 총 {}건 검색되었습니다".format(searchNum))
print("suhan은 총 {}건 검색되었습니다".format(htmlText.count('suhan')))

# 이미지 파일 다운로드
urlPNG = "https://suhan8984.github.io/img/imagination.PNG"
data = requests.get(urlPNG)
with open('sample/dasigeum.png', 'wb') as f:
    f.write(data.content)

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

# 등장인물의 이름: 녹색
nameList = soup.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.string)

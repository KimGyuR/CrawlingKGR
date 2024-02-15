from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

princeList = soup.find_all(string='the prince')
print(princeList)
print('the prince count:', len(princeList))

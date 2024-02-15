from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id': 'giftList'})
print('children 개수:', len(list(table_tag.children)))
for child in table_tag.children:
    print(child)
    print('-'*30)
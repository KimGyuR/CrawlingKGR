from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
count = 0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find('p').text)
        #print(bs.find('div', attrs={'id': 'mw-content-text'}).find('p').text)
    except AttributeError as e:
        print('this page is missing something! Continuing:  ', e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']
                print('-'*40)
                count += 1
                print(f'[{count}]: {newPage}')
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY')
bs = BeautifulSoup(html.read(), 'html.parser')

""" 출력항목
– <p class=“period-name”>”Tonight”</p>
– <img src=“…”	title=“Tonight:	Patchy	fog	between	4am	and	5am.	…”	>	
– <p class=“short-desc”	.	.	.>	Partly Cloudy <br>then Patch <br>Fog </p>
– <p class=“temp	temp-low”>Low	46	℉	</P>
"""

# 두 가지 다 출력 내용 동일
# find(), find_all() 함수를 이용하여 스크레이핑
def scraping_use_find(html):
    link_tags = bs.find_all('p', {'class': ['period-name', 'short-desc', 'temp temp-low']})
    for link in link_tags:
        print('-' * 50)
        print('[Period]: ', link.text)
        print('[Short desc]: ', link.text)
        print('[Temperature]: ', link.text)
        print('[Image desc]: ')

# select(), select_one() 함수를 이용하여 스크레이핑
def scraping_use_select(html):
    p_all = bs.select('p.period-name')
    for p in p_all:
        print('[Period]: ', p.text)

    p_all1 = bs.select('p.short-desc')
    for p in p_all1:
        print('[Short desc]: ', p.text)

    p_all2 = bs.select('p.temp temp-low')
    for p in p_all2:
        print('[Temperature]: ', p.text)


#scraping_use_find(html)

scraping_use_select(html)
from bs4 import	BeautifulSoup
from selenium import webdriver
import collections
collections.Callable = collections.abc.Callable

driver = webdriver.Chrome() #괄호 안에 /usr/local/bin/chromedriver 들어가 있으면 mac이나 이전 버전은 되나 현재 버전은 안됨, 버전 차이로 인한 오류
driver.get('https://www.coffeebeankorea.com/store/store.asp')

# 팝업창 생성됨
driver.execute_script('storePop2(1)')

# 현재의 html	소스를 저장
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())	#	HTML	소스를 보기 좋게 출력

store_names = soup.select('div.store_txt >	p.name >	span')
store_name_list = []
for	name in	store_names:
    store_name_list.append(name.get_text())

print('매장 개수:	',	len(store_name_list))
print(store_name_list)

store_addresses =	soup.select('p.address >	span')
store_address_list =	[]
for	addr in	store_addresses:
	print(addr.get_text())
	store_address_list.append(addr.get_text())
driver.quit()
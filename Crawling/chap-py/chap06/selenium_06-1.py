from bs4 import BeautifulSoup
from selenium import webdriver
import collections
collections.Callable = collections.abc.Callable

driver = webdriver.Chrome() # 예제에 적혀있는 /usr/local/bin/chromedriver mac에선 되나 window에선 안됨 업데이트로 인한 버전 차이가 이유
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(1)')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

store_names = soup.select('div.store_txt > p.name > span')
store_names_list = []
for name in store_names:
    store_names_list.append(name.get_text())

print('매장 개수: ', len(store_names_list))
print(store_names_list)

store_addresses = soup.select('p.address > span')
store_address_list = []
for addr in store_addresses:
    print(addr.get_text())
    store_address_list.append(addr.get_text())

driver.quit()
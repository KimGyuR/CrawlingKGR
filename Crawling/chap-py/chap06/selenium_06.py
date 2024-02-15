from bs4 import BeautifulSoup
from selenium import webdriver
import collections
collections.Callable = collections.abc.Callable

driver = webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(1)')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
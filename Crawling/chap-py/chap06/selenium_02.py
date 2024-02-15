from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

name = driver.find_element(By.CLASS_NAME,' green')
print(name.text)

print('-'*20)

nameList = driver.find_elements(By.CLASS_NAME, 'green')
for name in nameList:
    print(name.text)

driver.quit()
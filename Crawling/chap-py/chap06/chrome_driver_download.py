from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.naver.com')
print(driver.current_url)

sleep(2)
driver.close()
driver.quit()
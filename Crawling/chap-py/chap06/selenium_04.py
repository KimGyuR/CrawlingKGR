from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python')
search_box.submit() # 검색 버튼 누름

# 검색어 전달 및 검색 시작 -----------------------------------------------
time.sleep(3)
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
print(len(search_results))
# --------------------------------------------------------------------

# 검색결과에서 <h3>태그값 가져옴 ------------------------------------------
for result in search_results:
    title_element = result.find_element(By.CSS_SELECTOR, "h3")
    title = title_element.text.strip()
    print(f"{title}")
# --------------------------------------------------------------------
driver.quit()
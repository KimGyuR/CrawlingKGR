from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')

print(driver.current_url)
print(driver.title)
print(driver.page_source)

driver.implicitly_wait(time_to_wait=5)
driver.close()
driver.quit()
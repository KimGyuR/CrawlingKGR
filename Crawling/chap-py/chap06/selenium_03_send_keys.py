from selenium import webdriver
from selenium.webdriver.common.by import By

agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' + user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')

driver.implicitly_wait(5)

driver.find_element(By.NAME, 'id').send_keys('kbkr504')
driver.find_element(By.NAME, 'pw').send_keys('grkim32!@')

driver.find_element(By.ID, 'log.login').click()

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행 
driver = webdriver.Chrome()
# 접속할 주소 
driver.get("https://www.selenium.dev/")

# id=main_navbar 요소 접근
id_element = driver.find_element(By.ID, 'main_navbar')
print(id_element.text)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행 
driver = webdriver.Chrome()
# 접속할 주소 
driver.get("https://prod.danawa.com/list/?cate=112758&shortcutKeyword=노트북")

# 노트북 상품명 접근 
notebook_names = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

for name in notebook_names:
    print(name.text)

time.sleep(10)
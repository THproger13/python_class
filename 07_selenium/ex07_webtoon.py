from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 네이버 웹툰 페이지 접속
driver.get("https://comic.naver.com/webtoon")
# 네이버 웹툰 제목 요소 접근 
titles = driver.find_elements(By.CLASS_NAME, 'text')
time.sleep(3)
for title in titles:
    print(title.text)
print(len(titles))    

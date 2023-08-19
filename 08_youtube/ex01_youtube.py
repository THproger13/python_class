from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
driver.get("https://www.youtube.com/") #driver에게 해당 url을 가져오도록 하기
time.sleep(10) # 소스 코드의 실행을 100초간 중지한다. 따라서 이후의 코드들은 해당하는 시간동안 실행을 안한다. 
# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    # print(title.text) # innerHTML 값 
    # print(title.tag_name) # 해당 요소의 태그 이름
    print(title.get_attribute("aria-label")) # 해당 요소의 aria-label 속성값 가져오기 
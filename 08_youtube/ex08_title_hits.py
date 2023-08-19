from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
driver.get("https://www.youtube.com/")
time.sleep(2)
# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    if title.get_attribute("aria-label") and title.text: # shorts 영상을 걸러내기 위한 조건문 
        # aria-label 속성값 가져오기 
        aria_label = title.get_attribute("aria-label")
        # print(aria_label)
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits = int(hits.replace(",",""))
        print("제목", title.text)
        print("조회수", hits)

time.sleep(1000)
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
driver.get("https://www.youtube.com/feed/trending")
time.sleep(2)
# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

title_list = []
hits_list = []

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
#제목, 조회수 리스트가 담긴 딕셔너리
crawling_result ={
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
#result.to_csv("./result.csv", encoding="utf-8-sig")
# 조회수 내림차순으로 정렬후 csv로 저장-chaining 메서드 (최근의 트렌드)
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")
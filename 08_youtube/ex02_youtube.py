# selenium으로 유튜브 검색결과 화면 접근하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 검색어를 콘솔에서 입력받기 
q = input("검색어를 입력하세요: ")

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
# driver.get("https://www.youtube.com/")
# 검색결과 페이지에 바로 접속 
# driver.get("https://www.youtube.com/results?search_query=뉴진스")

# 콘솔에서 입력받은 검색어 적용 
driver.get("https://www.youtube.com/results?search_query=" + q)

time.sleep(2)
# 검색창 요소 접근
# search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력 
# search_input.send_keys("뉴진스")
# 검색 버튼 요소 접근 
# search_button = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# 검색 버튼 클릭
# search_button.click()

# 엔터 치기
# search_input.send_keys(Keys.RETURN)

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
    print(title.text) # innerHTML 값 

time.sleep(5)

# https://www.youtube.com/results?search_query=뉴진스
# https://www.youtube.com/results?search_query=아이브
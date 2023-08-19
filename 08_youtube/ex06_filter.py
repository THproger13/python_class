from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 유튜브 홈페이지 접속
# 2. 검색어 입력 
# 3. 엔터
# 4. 필터 클릭
# 5. 조회수 클릭
# 6. 무한 스크롤 
# 7. 제목 수집 

def scroll_fun():
    while True:
        # 스크롤 하기 전 높이 
        before_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 현재 높이 만큼 스크롤 내리기 
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        # 스크롤 내린 후 높이 
        after_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 스크롤 전, 후 높이 비교 
        if before_scroll == after_scroll:
            break

# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 페이지 접속
driver.get("https://www.youtube.com/")
time.sleep(2)
# 검색창 요소 접근
search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력 
search_input.send_keys("뉴진스")
# 엔터 치기
search_input.send_keys(Keys.RETURN)

time.sleep(2)

# 필터 버튼 요소 접근 
filter_button = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
# 필터 버튼 클릭 
filter_button.click()

# 조회수 클릭 (full XPATH 사용)
hits = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
hits.click()

# 무한 스크롤 함수를 호출하여 제목만 출력해봅시다. 
scroll_fun()
time.sleep(2)

# 제목 가져오기
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# 제목 출력
for title in titles:
    print(title.text) 

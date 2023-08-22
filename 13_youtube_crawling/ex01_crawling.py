from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

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
# 유튜브 인기급상승 페이지 접속
driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
time.sleep(2)

# 무한 스크롤 함수 호출 
scroll_fun()

# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# 제목 저장을 위한 리스트 
title_list = []

# 조회수 저장을 위한 리스트 
hits_list = []

for title in titles:
    # shorts 영상, YouTube 영화, 제목데이터 없는 컨텐츠 
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): 
        aria_label = title.get_attribute("aria-label")
        # rfind()메서드는 문자열 내에서 특정 부분 문자열을 찾아 해당 부분 문자열이 나타나느 가장 마지막 위치를 반환한다.
        # 'r'은 reverse의 약자이며, 역순으로 문자열을 탐색한다. 
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]

        # 조회수 값 범위에 따라 분리 
        # 조회수 없는 영상은 0으로, 조회수가 1000미만인 영상은 , 처리 생략 
        # 조회수 1,000 이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상 
        elif not hits:
            hits = 0
        # 조회수 1,000 미만 
        else:
            hits = int(hits)    
        
        # 동일한 제목 영상은 한 번만 
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

# 제목, 조회수 리스트가 담긴 딕셔너리 
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")
# 조회수 내림차순으로 정렬 후 csv로 저장 
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")


# 제목데이터의 명사저장을 위한 리스트
title_noun_list = []

# 제목 데이터의 형용사 저장을 위한 리스트
title_adjective_list = []

#title_list = result

okt = Okt()

'''
명사(Noun), 형용사(Adjective)만 따로 출력
 이때 title_list는 리스트 자료형이어서 okt.pos()가 분석을 못한다. 
 따라서 title_list 안의 문자열 요소들을 공백으로 구분해 하나의 문자열로 합친뒤
 okt.pos()가 띄어쓰기를 기준으로 단어들을 분석하도록 한다. 
'''
 
for word, tag in okt.pos(" ".join(title_list)):
    if tag in ['Noun', 'ProperNoun', 'Adjective']:
        if len(word) > 1:  # 한 글자는 제외
            if tag in ['Noun', 'ProperNoun']:
                title_noun_list.append(word)
            else:
                title_adjective_list.append(word)

# 같은 단어 노출 빈도를 명사, 형용사 따로 집계해서 변수로 저장하기
title_noun_list_count = Counter(title_noun_list)
title_adjective_list_count = Counter(title_adjective_list)


# 워드클라우드 객체 생성
wc = WordCloud(font_path='malgun', width =400, height=400)
'''
Counter로 분석한 데이터를 워드 클라우드로 만들기
    - **를 사용하여 "키워드 매개변수 언패킹"을 한다. 
    - title_noun_list_count에 title_adjective_list_count의 내용을 풀어서(언패킹) 추가를 해준다. 
    - 이렇게 함으로써 명사 빈도수와 형용사 빈도수가 합쳐진 하나의 딕셔너리가 생성된다.
'''
 
result = wc.generate_from_frequencies(dict(title_noun_list_count, **title_adjective_list_count))

#matplotlib으로 이미지 출력
#x,y축은 필요 없으므로 생략
plt.axis('off') 
plt.imshow(result)
#출력된 이미지를 꺼야 파일 저장됨
plt.show()
#워드 클라우드 파일 저장
wc.to_file('wordcloud_result.png')







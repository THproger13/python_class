from wordcloud import WordCloud

from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

okt = Okt()
text = "안녕하세요. 파이썬 입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재미있습니다.안녕하세요 크롤링 재미있습니다."

# 명사와 형용사인 부분만 리스트에 저장하기
word_list = []
#명사(Noun), 형용사(Adjective)만 따로 출력
for word, tag in okt.pos(text):
   
    if tag in ['Noun','Adjective']: #명사, 형용사 모두 
        print(word, tag)
        word_list.append(word)

# 같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 워드클라우드 객체 생성
wc = WordCloud(font_path='malgun', width =400, height=400)

#Counter로 분석한 데이터를 워드 클라우드로 만들기
result = wc.generate_from_frequencies(word_list_count)

#matplotlib으로 이미지 출력
plt.axis('off') #x,y축은 필요 없으므로 생략
plt.imshow(result)
#출력된 이미지를 꺼야 파일 저장됨
plt.show()
#워드 클라우드 파일 저장
wc.to_file('wordcloud_result.png')
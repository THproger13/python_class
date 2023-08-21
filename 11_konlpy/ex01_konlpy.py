from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter

#Kkma 모듈 객체 선언
kkma = Kkma()

#u는 한글이 깨지지 않게 하기 위함
#print(kkma.morphs(u'안녕하세요 반갑습니다.'))
#print(kkma.nouns(u'안녕하세요 반갑습니다.'))
#print(kkma.pos(u'안녕하세요 반갑습니다.'))

okt = Okt()
#print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
#print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
#print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
#print(okt.normalize(u'안녕하세욬ㅋㅋㅋㅋ')) # 맞춤법에 맞춰 바꿔줌

text = "안녕하세요. 파이썬 입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재미있습니다.안녕하세요 크롤링 재미있습니다."
# 단어와 종류를 분리
for word, tag in kkma.pos(text):
    print(word, tag)
for word, tag in okt.pos(text):
    print(word, tag)

# 명사와 형용사인 부분만 리스트에 저장하기
word_list = []
#명사, 형용사만 따로 출력
for word, tag in okt.pos(text):
    #if tag in 'Noun':  # 명사만
    #if tag in 'Adjective':  # 형용사만
    if tag in ['Noun','Adjective']: #명사, 형용사 모두 
        print(word, tag)
        word_list.append(word)

print(word_list)        

#Counter로 text 문장 횟수 출력 - 문장의 한 음절마다 몇번씩 출력되었는지 딕셔너리 형태로 출력
print(Counter(text))

text_list = ['파랑', '빨강', '노랑', '빨강', '파랑' , '초록', '빨강']
print(Counter(text_list))

#형태소 분석 결과를 Counter로 세어보기
print(Counter(word_list))







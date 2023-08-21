import pandas as pd
#성적 다루는 간단한 예제
#학번 정보

student_number = [1,2,3,4,5]

score_java = pd.Series([98,96,84,58,67], index = student_number)
score_python = pd.Series([88,100,92,55,70], index = student_number)


print(score_java)
print(score_python)

#java, python 시리즈 합계
total = score_java + score_python
print(total)

#순서가 뒤죽박죽인 시리즈
score_js = pd.Series([30,20,10,40,50], index =[3,2,1,4,5])
print(score_js)

#인덱스 값 기준으로 정렬하여 출력
#print(score_js.sort_index())

#java, python,js 총 합계
# 결국에는 인데스의 순서는 중요하지 않다. 인덱스의 값 자체를 기준으로 요소들의 합계를 구한다. 
total = score_java + score_python + score_js
print(total)

# index 기준 내림차순 정렬
print(total.sort_index(ascending=False))

#값기준 오름차순 정렬
print(total.sort_values())

#값기준 내림차순 정렬
print(total.sort_values(ascending=False))





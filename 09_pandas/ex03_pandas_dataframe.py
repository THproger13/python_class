import pandas as pd
'''
scores = pd.DataFrame(
    [
        [96,76,60,85,80], # java
        [88,58,74,96,97], # python  
        [77,59,98,97,84]  # js
    ]
)
#print(scores)

#행번호에 index값을 임의로 지정해준다. 
scores = pd.DataFrame(
    [
        [96,76,60,85,80], # java
        [88,58,74,96,97], # python  
        [77,59,98,97,84]  # js
    ],
    index = ["java", "python", "js"]
)
#print(scores)
'''



'''scores = pd.DataFrame(
    [
        [96,76,60], 
        [88,58,74],    
        [77,59,98],
        [10,58,95],
        [94,85,74]   
    ],
    index = student_number
)
#print(scores)

#{}를 사용해 각 column title을 준다.
scores = pd.DataFrame(
    {
        "java" : [96,76,60,85,80], # java
        "python" : [88,58,74,96,97], # python  
        "js" : [77,59,98,97,84]  # js
    },
    index = student_number
)
#print(scores)

#딕셔너리 데이터를 DataFrame으로 변환
scores_dict = {
    "java" : [96,76,60,85,80], # java
    "python" : [88,58,74,96,97], # python  q
    "js" : [77,59,98,97,84]  # js
}
scores =pd.DataFrame(scores_dict)
#print(scores)


scores = pd.DataFrame(
    {
        "java" : [96,76,60,85,80], # java
        "python" : [88,58,74,96,97], # python  
        "js" : [77,59,98,97,84]  # js
    },
    index = student_number
)
#print(scores)

# 이름 데이터 추가
scores["이름"] = ["김파이", "이파이", "박파이", "최파이", "정파이"]
#print(scores)

#데이터 추가 - 하나의 시리즈를 데이터 프레임에 추가한 형태이다.
scores.loc[6] = [80, 88, 88,"조파이"]
#print(scores) 
'''
#학번, 이름, 성적을 모두 포함한 DataFrame선언
student_number = [1,2,3,4,5,6]
scores = pd.DataFrame(
    {
        "이름" : ["김파이", "이파이", "박파이", "최파이", "정파이","조파이"],
        "java" : [96,76,60,85,80,100], # java
        "python" : [88,58,74,96,97,100], # python  
        "js" : [77,59,98,97,84,100]  # js
    },
     index=student_number
)

print(scores)

#index기준 정렬
print(scores.sort_index())


#index기준 내림차순 정렬
print(scores.sort_index(ascending=False))
# "이름"열 기준 오름차순 정렬
print(scores.sort_values(by="이름",ascending=True))

# "python"열 기준 오름차순 정렬

print(scores.sort_values(by="python",ascending=True))

#첫 2줄만 조회
print(scores.head(2))
#마지막 2줄만 조회
print(scores.tail(2))

# DataFrame을 csv로 내보내기
scores.to_csv("./scores.csv", encoding="utf-8-sig")



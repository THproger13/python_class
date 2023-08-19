# 딕셔너리(dictionary): 매핑형(key, value)
word_dic = {
    "dog": "강아지",
    "cat": "고양이",
    "tiger": "호랑이",
    "lion": "사자"
}
print(word_dic)
print(word_dic["dog"])
# 기존 value 수정
word_dic["dog"] = "멍멍이"
# 새로운 데이터 추가
word_dic["bear"] = "곰"
import pandas as pd

#series 선언
series1 = pd.Series([2,4,6,8,10])
print(series1)

#index를 지정
series2 = pd.Series([2,4,6,8,10], index=[1,2,3,4,5])
print(series2)

# range로 index를 지정

series3 = pd.Series([2,4,6,8,10], index = range(1,6))
print(series3)

# index용 리스트- 원하는 인덱스 값을 미리 변수로 설정해 시리즈의 인덱스로 지정

index_value = [10,11,12,13,14]
series4 = pd.Series([2,4,6,8,10], index=index_value)
print(series4)

# 데이터, index를 따로 선언 후 활용
data_value = [1,34,45,6,324]
index_value = [10,11,12,13,14]
series5 = pd.Series(data_value, index=index_value)
print(series5)
# 자바의 scanner 처럼 실행 후 콘솔에서 숫자를 입력받아 
# 홀수, 짝수를 판별하여 출력하는 코드를 작성하시오. 
num = int(input("숫자를 입력하세요: "))
print("입력값: ", num)
print("입력값의 타입: ", type(num))
if num%2 == 1:
    print("홀수입니다.")
elif num%2 == 0:
    print("짝수입니다.")

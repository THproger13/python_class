# 구구단 함수를 ex03_function.py 에 각각 정의하고
# main에서 1,2 번 선택을 받아 세로형, 가로형을 각각 
# 출력할 수 있도록 하시오. 

from ex03_function import *

while run:
    sel = int(input("선택: "))
    if sel == 1:
        # print("1번 선택")
        fun1()
    elif sel == 2:
        # print("2번 선택")
        fun2()
    elif sel == 3:
        print("종료")
        run = False

print("종료되었습니다.")
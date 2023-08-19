# while True:
#     print("ㅎㅎㅎ")

count = 1
while count <= 10:
    print("안녕하세요", count)
    count = count + 1

count = 1
while True:
    print("안녕하세요", count)
    if count == 10:
        break
    count = count + 1

count = 1
con = True
while con:
    print("안녕하세요", count)
    if count == 10:
        con = False
    count = count + 1
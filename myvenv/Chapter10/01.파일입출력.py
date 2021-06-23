# 1. 파일 쓰기
file = open("./myvenv/Chapter10/data.txt", "w", encoding="utf8")
file.write("1. 스타트코딩과 함께 파이썬 공부")
file.close()

# 2. 파일 추가
file = open("./myvenv/Chapter10/data.txt", "a", encoding="utf8")
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()

# 3. 파일 읽기
file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()
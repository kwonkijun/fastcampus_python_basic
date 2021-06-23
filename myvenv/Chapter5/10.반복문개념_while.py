# while
# : 보통 반복 횟수가 정해지지 않았을 때 사용한다.

i = 0 # 초기식
while i < 10: # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 2 # 증감식

# 무한루프
# : 조건식에 True를 넣어서 항상 반복되게 만든 것.

while True:
    x = input("종료하려면 exit를 입력하세요 >>>")
    if x == "exit":
        break
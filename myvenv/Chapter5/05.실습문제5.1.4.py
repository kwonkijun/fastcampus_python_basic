# 실습문제 5.1.4

korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))

total = korean + math + english
avg = total / 3

# 방법 1 
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")


# 방법 2
if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
    print("잘못 입력하였습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")

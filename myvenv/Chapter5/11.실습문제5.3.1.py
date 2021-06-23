# 실습문제 5.3.1
# 구구단 출력하기

x = int(input("몇 단을 출력할까요? >>>"))

for i in range(1, 10):
    print(x, "*", i, "=", x*i)
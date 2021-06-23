# 실습문제 4.3.1
# 사용자로부터 두개의 숫자를 입력 받고,
# 더한 결과를 출력하기

x = input("첫번째 숫자를 입력하세요 >>>")
y = input("두번째 숫자를 입력하세요 >>>")

# 자료형 확인하기 : type(x)
# str = string = 문자열

# 숫자형으로 변환
# int 함수를 사용 : int(데이터)

result = int(x) + int(y)
print(result)
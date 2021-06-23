# raise 구문을 사용해서 에러를 강제로 발생시켜 봅시다.

try:
    num = int(input("음수를 입력해 주세요>>>"))
    if num >= 0:
        raise ValueError("양수는 입력 불가")
except ValueError as e:
    print("에러 발생!", e)

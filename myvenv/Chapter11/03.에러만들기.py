class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")

try:
    num = int(input("음수를 입력해 주세요>>>"))
    if num >= 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생!", e)
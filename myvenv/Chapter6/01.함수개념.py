# 함수를 사용하는 이유

# 함수를 사용하지 않은 경우
print("안녕하세요. 동준님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. 현식님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요. 원준님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

print("안녕하세요. 길동님")
print("현재 프리미엄 서비스 사용기간이 5일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, date):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")

printMessage("동준", 30)
printMessage("현식", 15)
printMessage("원준", 7)
printMessage("길동", 5)
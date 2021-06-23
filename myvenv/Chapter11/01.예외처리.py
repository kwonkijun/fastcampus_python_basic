# 원화를 입력, 환율 입력 -> 달러값

won = input("원화금액을 입력 하세요>>>")
dollar = input("환율을 입력 하세요>>>")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 파일 닫기
    print("예외가 발생하던지, 발생하지 않던지 항상 실행되는 코드")
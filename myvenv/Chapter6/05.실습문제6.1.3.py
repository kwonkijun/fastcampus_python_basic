# 실습문제 6.1.3
# 로또 번호 추출기
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = [] # 로또 번호를 저장할 리스트 

count = 0 # 현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = get_random_number()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")
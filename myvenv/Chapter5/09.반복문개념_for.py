# 반복문
# : 반복해서 명령을 사용하고 싶을 때

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
# - 리스트 사용
champions = ["티모", "이즈리얼", "리신"]

for champion in champions:
    print("선택한 챔피언은", champion, "입니다.")

# - 문자열 사용
fighting_message = "자신감을 가지자! 나에게 한계란 없다!"

for word in fighting_message:
    print(word)

# - range 객체 사용
# range(10) -> 0~9까지 숫자를 포함하는 range 객체나온다. 0,1,2,3,4,5,6,7,8,9
# range(시작, 끝+1, 단계)
for i in range(1, 10, 2):
    print(i)
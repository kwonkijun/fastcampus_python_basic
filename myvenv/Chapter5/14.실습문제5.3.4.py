# 실습문제 5.3.4
# Learning Korean ver 2.0

# 한국어 리스트
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# 점수
score = 0

print("Let's Learning Korean")
for word in word_list:
    print(word)
    data = input()
    if data == word: # 문제를 맞힌 경우
        score += 1 # 점수를 1 증가

print("전체 문제 개수 : ", len(word_list))
print("맞힌 개수 : ", score)
print("틀린 개수 : ", len(word_list) - score)

# 전체 문제 개수: 4 개
# 맞힌 문제 개수: 2 개
# 틀린 문제 개수: 2 개

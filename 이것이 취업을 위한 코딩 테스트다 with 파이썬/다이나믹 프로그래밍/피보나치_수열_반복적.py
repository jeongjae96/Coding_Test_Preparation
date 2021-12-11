'''
top-down/memoization/하향식
bottom-up/상향식

DP 테이블: bottom-up 방식에서 사용되는 결과 저장용 리스트
memoization은 top-down에 국한되어 사용되는 표현. 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미. DP와는 별도의 개념.
'''

d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

# 피보나치 함수 반복문으로 구현(보텀업 DP)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
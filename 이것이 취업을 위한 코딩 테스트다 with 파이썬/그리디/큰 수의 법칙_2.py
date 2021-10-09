# 더 효율적인 풀이법.

# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

# 반복되는 수열
# first + ... + first + second : 길이는 K+1.

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k + m % (k + 1)

result = count * first + (m - count) * second

print(result)

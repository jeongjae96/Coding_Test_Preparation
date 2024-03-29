# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 두 번째 연산은 N이 K로 나누어떨어질 때만 가능.

# 1. N에서 1을 뺀다.
# 2. N을 K으로 나눈다.

# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성.

n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    
    # K로 나누기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
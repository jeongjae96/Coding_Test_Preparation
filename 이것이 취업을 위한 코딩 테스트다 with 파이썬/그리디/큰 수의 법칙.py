# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 아래에 주어지는 큰 수의 법칙에 따른 결과를 출력하시오.

# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.

# 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.

# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0: break

    result += second
    m -= 1

print(result)
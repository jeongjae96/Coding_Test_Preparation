# 수열 내림차순 정렬

# 첫째 줄에 수열의 갯수
# 두번째 줄부터 N개의 수 입력

# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []

for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
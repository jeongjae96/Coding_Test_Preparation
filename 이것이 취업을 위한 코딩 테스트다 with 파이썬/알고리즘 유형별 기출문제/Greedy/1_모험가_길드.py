'''
공포도 X인 모험가는 반드시 X명 이상으로 구성.
몇 개의 모험가 그룹을 만들 수 있는지. (최댓값)
'''

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0 # 총 그룹의 수

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기

    if count >= i:
        result += 1
        count = 0

print(result)
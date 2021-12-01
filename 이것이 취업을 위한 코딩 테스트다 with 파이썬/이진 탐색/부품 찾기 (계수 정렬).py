n = int(input())
array = [0] * 1000001 # 1 <= N <= 1,000,000

for i in input().split():
    array[int(i)] = 1

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
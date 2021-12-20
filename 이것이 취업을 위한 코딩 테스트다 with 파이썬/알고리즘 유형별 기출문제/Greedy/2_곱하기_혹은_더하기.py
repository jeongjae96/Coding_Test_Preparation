'''
0~9로 이루어진 문자열 S. (1 <= len(S) <= 20)
사이사이에 'x' or '+'. (연산은 왼쪽에서부터 순서대로)

가장 큰 수.

0/1일 경우 더하기.
'''

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
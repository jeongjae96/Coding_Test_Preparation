# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    # x*3인 이유는 x*2일 경우 9, 991 같은 경우 991이 더 앞편에 정렬되기 때문
    
    answer = str(int(''.join(numbers)))
    # int로 변환하는 이유는 numbers가 ['0', '0', '0', '0']일 경우 '0000'을 0으로 변환하기 위해
    
    return answer
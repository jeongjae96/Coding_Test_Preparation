from itertools import permutations
import math

def check(n):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = []
    
    for k in range(1, len(numbers)+1):
        per_list = list(map(''.join, permutations(list(numbers), k)))
        
        for i in list(set(per_list)): # set으로 중복된거 줄이기
            if check(int(i)):
                answer.append(int(i))
                
    answer = len(set(answer)) 
    # numbers에 0이 들어가 있는 경우 int 사용 시 중복된 경우 생길 수 있음.
    # 예시 "011"의 경우 11과 011 같은 숫자 취급.
    
    return answer
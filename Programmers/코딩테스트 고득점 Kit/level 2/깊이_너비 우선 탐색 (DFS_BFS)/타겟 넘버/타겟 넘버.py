# product(*list) : 배열 안의 배열들로 만들 수 있는 조합을 모두 만든다.
# Asterisk(*)을 넣어야 한다. *는 Unpacking을 위함이다.

from itertools import product

def solution(numbers, target):
    answer = 0
    
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    
    answer = s.count(target)
    
    return answer
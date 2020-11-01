# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    answer = 0
    
    above = 0
    below = 0
    
    citations.sort()
    
    # 논문 n편 중, 인용된 횟수가 h편 이상 또는 이하여야 하므로, H-Index는 0 이상 n 이하.
    for h in range(len(citations)+1): 
        above = sum(i >= h for i in citations) # h번 이상 인용된 논문 수
        below = sum(i <= h for i in citations) # h번 이하 인용된 논문 수
        
        if above >= h and below <= h:
            answer = h
    
    return answer
# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42578

# 추가로 더 입거나 변경

from collections import Counter

def solution(clothes):
    
    clothes_list = list()
    
    for cloth in clothes:
        clothes_list.append(cloth[-1])
    
    clothes_count = Counter(clothes_list)
    
    if len(clothes_count) == 1:
        return list(clothes_count.values())[0]
    else:
        cnt = 1
        for v in list(clothes_count.values()):
            cnt *= (v+1) # 안 입는 경우도 추가
        
        return cnt-1 # 모두 안 입은 경우 제외

# 참고
# https://deepwelloper.tistory.com/129
# https://eda-ai-lab.tistory.com/472
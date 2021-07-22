# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42626

# 힙 큐 알고리즘: https://python.flowdas.com/library/heapq.html#heapq.heapify

import heapq

def solution(scoville, K):
    answer = 0
    
    h = heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        
    return answer

# 참고: https://liveyourit.tistory.com/191
# https://wooaoe.tistory.com/81
# 참고: https://www.youtube.com/watch?v=qA-wy00bQv4
# heapq: https://www.daleseo.com/python-heapq/

import heapq

def solution(jobs):
    # jobs가 작업이 요청되는 시점 순으로 입력되어 있을 보장이 없기 때문에 정렬을 해준다.
    jobs.sort()
    # beginning : 현재 작업의 시작 시간을 넣을 예정.
    count, beginning = 0, -1
    wait = []
    # p_time : 현재 시간
    p_time = jobs[0][0]
    length = len(jobs)
    answer = 0
    
    while count < length:
        for s, t in jobs:
            if beginning < s <= p_time:
            # beginning < s and s <= p_time:
                heapq.heappush(wait, (t, s))
        
        if len(wait) > 0:
            beginning = p_time
            time_r, start = heapq.heappop(wait)
            count += 1
            p_time += time_r
            answer += p_time - start
        else:
            p_time += 1
    
    return answer // length
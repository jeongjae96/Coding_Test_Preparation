from collections import deque, Counter

def solution(progresses, speeds):
    
    progresses_q = deque(progresses)
    speeds_q = deque(speeds)
    
    day = 0
    day_list = list()
    
    while progresses_q:
        if progresses_q[0] >= 100:
            progresses_q.popleft()
            speeds_q.popleft()
            day_list.append(day)
        else:
            day += 1
            progresses_q = deque([x + speeds_q[i] for i,x in enumerate(progresses_q)])
    
    answer = list(Counter(day_list).values())

    return answer
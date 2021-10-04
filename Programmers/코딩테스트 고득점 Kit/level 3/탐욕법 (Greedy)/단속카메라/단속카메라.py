# 참고: https://blog.naver.com/paula23/222097454798

def solution(routes):
    
    routes = sorted(routes, key=lambda x : x[0])
    
    start, end = routes[0][0], routes[0][1]
    
    answer = 1
    
    for s, e in routes[1:]:
        if s <= end:
            start = s
            end = min(e, end)
        else:
            start, end = s, e
            answer += 1
    
    return answer
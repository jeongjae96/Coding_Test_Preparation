def solution(n, times):
    # binary search를 위한 sorting
    times.sort()

    # 최소시간 (기다리는 사람 1명, 심사 시간 1분 일 때)
    min_time = 1
    
    # 최대시간 (기다리는 사람 모두 심사시간이 가장 긴 심사관에가 갈 때)
    max_time = max(times) * n
    
    answer = max_time
    
    while(min_time <= max_time):
        # 한 심사관에게 주어진 시간
        mid_time = (min_time + max_time) // 2
        
        sum = 0
        
        # mid time일 때, 몇 명 검사할 수 있을지 체크
        for i in times:
            sum += mid_time // i
            
        # n명 이상 검사할 수 있을 경우 최대시간 감소
        if(sum >= n):
            answer = mid_time
            max_time = mid_time - 1
        # n명보다 적게 검사할 수 있을 경우 최소시간 증가
        else:
            min_time = mid_time + 1
            
    
    return answer
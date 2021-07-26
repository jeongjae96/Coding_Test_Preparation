# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. => lost와 reserve에 같은 값이 있다면, reserve와 lost에서 제외.

def solution(n, lost, reserve):
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    # 차집합 연산으로 제외
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
        
    answer = n - len(lost_set)
    
    return answer
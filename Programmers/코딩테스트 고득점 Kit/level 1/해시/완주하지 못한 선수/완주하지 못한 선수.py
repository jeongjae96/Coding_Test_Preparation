# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주.
# 참고: https://blog.naver.com/caeruleum00/222085710645

def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant[-1]
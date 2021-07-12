# 출처: https://programmers.co.kr/learn/courses/30/lessons/42860

import string

def solution(name):
    
    # 'N' 포함 이전 문자는 위 방향, 이후 문자는 아래방향.
    answer = sum([ord(a)-ord('A') if a <= 'N' else ord('Z')-ord(a)+1 for a in name])
    
    # name의 알파벳 중 'A'가 아닌 알파벳('B'~'Z')의 위치를 반환
    # 즉, 이동해서 문자를 바꿔야 하는 위치.
    idxBZ = [i for i in range(len(name)) if name[i] != 'A']
    
    cur = 0
    
    while idxBZ != []:
        # 'A'가 아닌 name의 어느 위치로 가는게 빠를지 판단.
        # == idxBZ의 처음 idx로 가는게 빠를지 마지막 idx로 가는게 빠를지 판단.
        
        # BZidx의 처음 idx에 도달하기 위해 왼쪽 또는 오른쪽으로 이동한다. 그 중 거리가 짧은 것을 택한다.
        leftmost = min(abs(idxBZ[0]-cur), len(name)-abs(idxBZ[0]-cur))
        # BZidx의 마지막 idx ~~
        rightmost = min(abs(idxBZ[-1]-cur), len(name)-abs(idxBZ[-1]-cur))
        
        if leftmost <= rightmost:
            cur = idxBZ.pop(0)
            answer += leftmost
            
        else:
            cur = idxBZ.pop()
            answer += rightmost
            
    return answer

# 참고: https://blog.naver.com/dnfla420/221842594794
# https://blog.naver.com/tutumd96/221755315575

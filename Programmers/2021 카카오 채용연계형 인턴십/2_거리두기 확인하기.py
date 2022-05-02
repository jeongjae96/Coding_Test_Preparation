# source: https://programmers.co.kr/learn/courses/30/lessons/81302

# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

'''
- 대기실 5개
- 각 대기실 크기 5x5
- 맨해튼 거리 2 초과로 앉기
- 파티션이 막혀있는 경우 괜찮다.
'''

'''
- places의 각 행은 하나의 대기실 구조
- P : 응시자 자리
- O : 빈 테이블
- X : 파티션
'''

def solution(places):
    
    answer = []
    
    # 코드의 리팩토링이 필요하다. 어차피 for문을 돌려 모든 경우의 수를 확인하기 때문에, 맨해튼 거리 2이하인 경우의 수를 반으로 줄여도 될 것 같다.
    # 맨해튼 거리가 2이하인 경우는 총 12 가지
    dx = [-2, -1, 1, 2, 0, 0, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 0, 0, -2, -1, 1, 2, -1, 1, -1, 1]
    
    for place in places:
        
        safe = 1
        
        for y in range(5):
            for x in range(5):
                
                if place[y][x] == 'P':
                    
                    for i in range(12):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        
                        if nx >= 0 and ny >= 0 and nx < 5 and ny < 5:
                            if place[ny][nx] == 'P':
                                # 다른 응시자와 세로/가로선 상 맨해튼 거리 2이하인 경우
                                # 응시자 사이 1개의 파티션만 있어도 안전.
                                if i < 8:
                                    if dx[i] == -2:
                                        if place[ny][nx+1] != 'X':
                                            safe = 0
                                    elif dx[i] == 2:
                                        if place[ny][nx-1] != 'X':
                                            safe = 0
                                    elif dy[i] == -2:
                                        if place[ny+1][nx] != 'X':
                                            safe = 0
                                    elif dy[i] == 2:
                                        if place[ny-1][nx] != 'X':
                                            safe = 0
                                    else:
                                        safe = 0
                                # 다른 응시자와 대각선 상 맨해튼 거리 1이하인 경우
                                # 응시자 사이 2개의 파티션이 있어야 한다.
                                else:
                                    if i == 8:
                                        if place[ny+1][nx] != 'X' or place[ny][nx+1] != 'X':
                                            safe = 0
                                    elif i == 9:
                                        if place[ny-1][nx] != 'X' or place[ny][nx+1] != 'X':
                                            safe = 0
                                    elif i == 10:
                                        if place[ny+1][nx] != 'X' or place[ny][nx-1] != 'X':
                                            safe = 0
                                    else:
                                        if place[ny-1][nx] != 'X' or place[ny][nx-1] != 'X':
                                            safe = 0
                                            
        answer.append(safe)
                                  
    return answer
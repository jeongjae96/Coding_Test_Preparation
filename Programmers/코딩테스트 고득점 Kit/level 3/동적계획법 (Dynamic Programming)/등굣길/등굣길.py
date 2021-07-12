# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    
    mod = 1000000007
    
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if ([x+1, y+1] in puddles) or ((x,y) == (0,0)):
                continue
            map[y][x] = (map[y-1][x] + map[y][x-1])
    
    answer = map[-1][-1] % mod
                
    return answer
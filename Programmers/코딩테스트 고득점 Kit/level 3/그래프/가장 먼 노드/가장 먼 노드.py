# 참고:  https://blog.naver.com/lopti_/222337041108

from collections import deque

def bfs(graph, start, visited):
    
    count = 0 
    
    q = deque([[start, count]])
    
    while q:
        v = q.popleft()
        
        start = v[0]
        count = v[1]
        
        if visited[start] == -1:
            visited[start] = count
            count += 1
            
            for x in graph[start]:
                q.append([x,count])
    
def solution(n, edge):  
    
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for i in edge:
        x = i[0]
        y = i[1]
        
        graph[x].append(y)
        graph[y].append(x)
        
    bfs(graph, 1, visited)
    
    for v in visited:
        if v == max(visited):
            answer+=1
    
    return answer
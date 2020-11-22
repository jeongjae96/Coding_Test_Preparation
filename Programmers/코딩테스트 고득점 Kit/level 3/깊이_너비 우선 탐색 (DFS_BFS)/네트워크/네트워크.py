# 참고: https://cocojelly.github.io/algorithm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-DFS-BFS-(2)/

def solution(n, computers):
    answer = 0 # 네트워크의 갯수를 저장할 변수
    bfs = [] # 탐색을 위한 큐
    visited = [0]*n # 방문한 노드를 체크해 둘 리스트
        
    while 0 in visited:
        x = visited.index(0) # index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
        bfs.append(x)
        visited[x] = 1
        
        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1 # 한 네트워크의 탐색을 마치면 개수 추가
        
    return answer
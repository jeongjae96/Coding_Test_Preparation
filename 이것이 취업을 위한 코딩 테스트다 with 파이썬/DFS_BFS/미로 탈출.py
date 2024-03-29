# N X M 크기의 직사각형 형태의 미로.
# 여러 마리의 괴물을 피해 탈출.
# 시작 위치: (1, 1), 출구 위치: (N, M)
# 한 칸씩 이동. 괴물 있는 부분 0, 없는 부분 1로 표시

#  탈출하기 위해 움직여야 하는 최소 칸의 개수 구하기. (시작 칸과 마지막 칸 포함 + 항상 1)

'''
해결법

BFS를 사용. BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문.
(1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
특정 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는 식으로.
'''

# 아래의 소스코드는 첫 번째 시작 위치는 다시 방문할 수 있도록 되어 값이 변경될 여지가 있으나 답을 도출하는 데에는 문제가 없다.
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물 있을 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m -1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
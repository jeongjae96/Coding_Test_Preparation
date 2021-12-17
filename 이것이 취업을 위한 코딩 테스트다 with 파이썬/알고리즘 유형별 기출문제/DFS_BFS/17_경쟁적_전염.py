'''
N X N 크기의 시험관. (1 X 1 크기의 칸으로 나누어져 있다)
특정한 위치에 바이러스 존재.
바이러스의 종류: 1~K

모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식.
매초 번호가 낮은 종류의 바이러스부터 증식.
특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에는 다른 바이러스 x.

시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, s초가 지난 후 (X, Y)에 존재하는 바이러스의 종류 출력. (존재하지 않는 다면 0 출력) (X: 행, Y: 열)

입력 조건
- 첫째 줄 자연수 N, K(1 <= N <= 200, 1 <= K <= 1,000)
- 둘째 줄, N개의 줄에 걸쳐서 시험관의 정보. 각 행은 N개의 원소로 구성, 바이러스의 번호가 주어지며 공백으로 구분.
- 바이러스 존재하지 않으면 0. (바이러스의 번호 <= K)
- N + 2번째 줄에는 S, X, Y (0 <= S <= 10,000, 1 <= X, Y <= N)

출력 조건
S초 뒤에 (X, Y)에 존재하는 바이러스의 종류 출력. (없으면 0 출력)
'''

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))

    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스의 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후 큐로 옮기기 (낮은 번호 먼저)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(n):
        nx = x + dx[i]
        ny = y + dy[i]

        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
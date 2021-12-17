'''
연구소 크기: N X M 직사각형 (1 X 1 크기의 정사각형으로 나누어져 있다)
빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나 차지.
일부 칸은 바이러스가 존재, 상하좌우 인접한 빈칸으로 퍼져나간다.
새로 세울 수 있는 벽의 개수는 무조건 3개.

연구소의 지도가 주어졌을 때, 얻을 수 있는 안전 영역 크기의 최댓값 구하기

입력 조건
- 첫째 줄: 지도의 세로 크기 N, 가로 크기 M. (3 <= N, M <= 8)
- 둘째 줄부터 N개의 줄에 지도의 모양. (0: 빈칸, 1: 벽, 2: 바이러스) (2 <= '2' <= 10) (빈 칸의 개수 3개 이상.)
'''

# 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때, DFS나 BFS를 적절히 이용.

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치 후, 재귀적 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1

                dfs(count)

                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
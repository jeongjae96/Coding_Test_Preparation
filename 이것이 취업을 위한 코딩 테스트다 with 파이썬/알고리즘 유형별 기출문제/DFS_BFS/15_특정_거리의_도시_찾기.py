'''
1~N번까지의 도시와 M개의 단방향 도로. (모든 도로 거리 1)
특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 정확히 K인 모든 도시의 번호 출력.

입력 조건
- 첫째 줄 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 번호 X
- 둘째 줄부터 M개의 줄에 걸쳐, 자연수 A B (공백으로 구분). A번 도시에서 B번 도시로 이동하는 단방향 도로 존재한다는 의미.

출력 조건
- 출력할 도시의 번호를 한 줄에 하나씩 오름차순으로.
- 하나도 존재하지 않으면 -1 출력.
'''

from collections import deque

# 도시, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정.

# 너비 우선 탐색(BFS) 실행
q = deque([x])

while q:
    now = q.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)
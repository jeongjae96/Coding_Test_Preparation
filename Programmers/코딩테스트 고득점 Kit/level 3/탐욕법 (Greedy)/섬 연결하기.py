# 참고: https://blog.naver.com/wizzle1/221890661178

def solution(n, costs):
    answer = 0
    
    # 비용의 오름차순으로 정렬.
    costs = sorted(costs, key=lambda x : x[2])
    
    # 섬 갯수만큼 리스트 생성.
    visited = [0] * n
    
    # 처음 섬은 방문한 걸로 1 설정.
    visited[costs[0][0]] = 1
    
    while sum(visited) != n:
        for cost in costs:
            s, e, c = cost
            
            if visited[s] or visited[e]:
                if visited[s] and visited[e]:
                    continue
                else:
                    visited[s] = 1
                    visited[e] = 1
                    
                    answer += c
                    break # break가 없다면 모든 비용이 다 더해진다.
    
    return answer
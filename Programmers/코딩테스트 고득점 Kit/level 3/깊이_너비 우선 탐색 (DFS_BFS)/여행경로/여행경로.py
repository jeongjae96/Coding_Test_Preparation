def solution(tickets):
    
    routes = dict()
    
    for (depart, dest) in tickets:
        routes[depart] = routes.get(depart, []) + [dest]
    
    # 스택 이용. pop을 통해 빼주므로 역순으로 정렬
    for i in routes.keys():
        routes[i].sort(reverse=True)
        
    stack = ["ICN"]
    answer = []
    
    while stack:
        top = stack[-1]
        
        # dictionary의 in은 key에 한해 동작.
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
            
        else:
            # pop하여 stack으로 넣기
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    answer.reverse()
    
    return answer
def solution(priorities, location):
    
    loc = [i for i in range(len(priorities))]
    
    print_ord = []
    
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            print_ord.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            
    answer = print_ord.index(location) + 1
    
    return answer
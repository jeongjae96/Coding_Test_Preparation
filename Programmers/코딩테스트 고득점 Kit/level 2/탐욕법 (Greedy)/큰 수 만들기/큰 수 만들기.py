def solution(number, k):
    
    stack = list()
    
    for num in number:
        while stack and num > stack[-1] and k > 0:
            
            stack.pop()
            k -= 1
        
        stack.append(num)
    
    # k개를 다 제거하지 못 했을 때,
    if k > 0:
        for i in range(k):
            stack.pop()
            
    answer = ''.join(stack)
    
    return answer
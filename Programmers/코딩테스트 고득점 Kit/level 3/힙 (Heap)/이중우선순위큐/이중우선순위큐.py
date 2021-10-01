# 참고: https://www.youtube.com/watch?v=_17ltnxxmGw
# 참고: https://blog.naver.com/hyunjiok10/222476856649

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        instruction, num = op.split(' ')
        num = int(num)
        
        if instruction == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
        else:
            if len(min_heap) == 0:
                pass
            elif num == 1:
                max_num = -heapq.heappop(max_heap)
                min_heap.remove(max_num)
            else:
                min_num = heapq.heappop(min_heap)
                max_heap.remove(-min_num)
                
    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    trucks_on_bridge = [0] * bridge_length
    weight_bridge_handling = 0
    
    # 효율성을 위해 truck_weights를 뒤집는다.
    # truck_weights.pop(0)는 첫 원소를 빼고 한 칸씩 앞으로 모두 땡기므로 O(n)
    # truck_weights.pop()은 O(1)
    truck_weights = truck_weights[::-1]
    
    while trucks_on_bridge:
        time += 1
        weight_bridge_handling -= trucks_on_bridge.pop()
        
        if truck_weights:
            if truck_weights[-1] + weight_bridge_handling <= weight:
                weight_bridge_handling += truck_weights[-1]
                trucks_on_bridge.insert(0, truck_weights.pop())
            else:
                trucks_on_bridge.insert(0,0)
    
    return time

# 참고: https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD-in-python
# https://sinsomi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD-%EC%B4%88%EC%BD%94%EB%8D%94
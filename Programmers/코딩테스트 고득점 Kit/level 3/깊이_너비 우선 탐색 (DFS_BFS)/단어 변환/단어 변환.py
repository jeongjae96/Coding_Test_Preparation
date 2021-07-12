# 문제 출처: # https://cocojelly.github.io/algorithm/프로그래머스-코딩테스트-연습-DFS-BFS-(3)/

# 알파벳 하나씩만 바꾸어 target 단어 만들기.
# words에서 begin (시작 단어)와 한 글자만 다른 단어를 찾아야 한다.
# words에서 begin과 하나씩 비교. 찾았다면, 그 다음 단어를 찾기 위해 words의 단어와 다시 하나씩 비교.
# words의 단어를 여러차례 순회하기 위해 BFS 사용.

from collections import deque

def convertible(a, b):
    
    # 알파벳이 같으면 0, 다르면 1로 체크하여 단어를 비교한 뒤 합을 낸다. 합이 1일 시, 알파벳이 하나만 다른 단어.
    if sum((1 if x != y else 0) for x,y in zip(a,b)) == 1:
        return True
    return False

def solution(begin, target, words):
    # BFS를 구현하기 위해 큐를 사용. 큐는 알파벳 하나씩 바꿔가는 단어를 표시해두기 위해 사용.
    q, d = deque(), dict()
    q.append((begin, 0))
    
    d[begin] = set(filter(lambda x : convertible(x, begin), words))
    
    for w in words:
        d[w] = set(filter(lambda x : convertible(x, w), words))
        
    while q:
        cur, level = q.popleft()
        
        # 큐의 단어를 모두 소비했음에도 target이 만들어지지 않았다면, 단어를 만들 수 없는 것이므로 0을 return.
        if level > len(words):
            return 0
        
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
                
    return 0

# 알파벳 하나씩만 바꾸어 target 단어 만들기.
# words에서 begin (시작 단어)와 한 글자만 다른 단어를 찾아야 한다.
# words에서 begin과 하나씩 비교. 찾았다면, 그 다음 단어를 찾기 위해 words의 단어와 다시 하나씩 비교.
# words의 단어를 여러차례 순회하기 위해 BFS 사용.

from collections import deque

def convertible(a, b):
    
    # 알파벳이 같으면 0, 다르면 1로 체크하여 단어를 비교한 뒤 합을 낸다. 합이 1일 시, 알파벳이 하나만 다른 단어.
    if sum((1 if x != y else 0) for x,y in zip(a,b)) == 1:
        return True
    return False

def solution(begin, target, words):
    # BFS를 구현하기 위해 큐를 사용. 큐는 알파벳 하나씩 바꿔가는 단어를 표시해두기 위해 사용.
    q, d = deque(), dict()
    q.append((begin, 0))
    
    d[begin] = set(filter(lambda x : convertible(x, begin), words))
    
    for w in words:
        d[w] = set(filter(lambda x : convertible(x, w), words))
        
    while q:
        cur, level = q.popleft()
        
        # 큐의 단어를 모두 소비했음에도 target이 만들어지지 않았다면, 단어를 만들 수 없는 것이므로 0을 return.
        if level > len(words):
            return 0
        
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
                
    return 0

# 참고: https://cocojelly.github.io/algorithm/프로그래머스-코딩테스트-연습-DFS-BFS-(3)/
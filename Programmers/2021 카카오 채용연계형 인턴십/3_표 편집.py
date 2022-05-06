# source: https://programmers.co.kr/learn/courses/30/lessons/81303
# ref: https://www.youtube.com/watch?v=A-KfaMVBfhg

'''
n: 표의 행 개수
k: 처음 선택된 행의 위치
cmd: 명령어가 담긴 문자열 배열

명령어
"U X": 현재 선택된 행에서 X칸 위에 있는 행 선택.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행 선택.
"C": 현재 선택된 행 삭제 후, 아래 행 선택. 삭제된 행이 마지막 행인 경우 바로 윗 행 선택.
"Z": 최근에 삭제된 행을 원래 그 자리로 복구. 선택된 행 바뀌지 않는다.
'''

# 모든 명령어 수행 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시.

# Linked list를 통한 효율성 개선
class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    answer = ''
    
    # 링크드 리스트 초기화
    nodeArr = [Node() for _ in range(n)]
    
    for i in range(1, n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]
    
    # 현재 노드
    curr = nodeArr[k]
    # removed 쌓아놓을 스택
    mystack = []
    
    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            
            for _ in range(x):
                curr = curr.prev
        
        elif str[0] == 'D':
            x = int(str[2:])
            
            for _ in range(x):
                curr = curr.next
        
        elif str[0] == 'C':
            mystack.append(curr)
            curr.removed = True
            
            up = curr.prev
            down = curr.next
            
            if up:
                up.next = down
            
            if down:
                down.prev = up
                curr = down
            # 삭제된 행이 마지막 행인 경우
            else:
                curr = up
        
        else:
            node = mystack.pop()
            node.removed = False
            
            up = node.prev
            down = node.next
            
            if up:
                up.next = node
            if down:
                down.prev = node
    
    for i in range(n):
        if nodeArr[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    
    return answer
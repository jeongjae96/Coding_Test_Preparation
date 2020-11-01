#문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    
    for c in commands:
        s_list = array[c[0] - 1 : c[1]]
        s_list.sort()
        answer.append(s_list[c[2]-1])
    
    return answer
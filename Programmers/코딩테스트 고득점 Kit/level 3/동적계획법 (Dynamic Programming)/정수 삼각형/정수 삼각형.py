# 출처: https://programmers.co.kr/learn/courses/30/lessons/43105

'''
				7				
			3		8			
		8		1		0		
	2		7		4		4	
4		5		2		6		5
'''

from copy import deepcopy

def solution(triangle):
    
    memo = deepcopy(triangle)
    
    for i in range(len(memo)-1):
        # 양 끝 값 메모
        memo[i+1][0] += memo[i][0]
        memo[i+1][-1] += memo[i][-1] 
        
        # 나머지 메모
        for j in range(1, i+1):
            memo[i+1][j] += max(memo[i][j-1], memo[i][j])
            
    answer = max(memo[-1])
    
    return answer

# 참고: https://blog.naver.com/kbsdr11/221606911092
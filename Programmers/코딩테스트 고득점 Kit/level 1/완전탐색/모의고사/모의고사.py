# https://itholic.github.io/kata-supo/

from itertools import cycle

def solution(answers):
    
    winner = []
    
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0, 0, 0]
    
    for s1, s2, s3, ans in zip(cycle(supo1), cycle(supo2), cycle(supo3), answers):
        if s1 == ans: scores[0] += 1
        if s2 == ans: scores[1] += 1
        if s3 == ans: scores[2] += 1
            
    for i, score in enumerate(scores):
        if score == max(scores):
            winner.append(i+1)
    
    return winner

# itertools cycle
# https://medium.com/@hckcksrl/python-itertools-cycle-module-f53ba30949ed
'''
예를들어 list1 = [ 1 , 2 , 3 , 4 ] , list2 = [ ‘a’ , ’b’ , ’c’ , ’d’ , ’e’ , ’f’ , ’g’ ] 가 있다고 할때 list1, list2 를 zip을 이용해 엮으려고 하면 list1 이 list2 보다 작기때문에 다시 처음으로 돌아가서 반복을 해야한다. 이것을 cycle 함수를 사용해 간단하게 구현을 할수 있다.
'''
# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
        else:
            str_num = ''
            
            while s[i].isalpha():
                str_num += s[i]
                i += 1
                
                if str_num in num_dict.keys():
                    
                    answer += num_dict[str_num]
                    break
            
    return int(answer)
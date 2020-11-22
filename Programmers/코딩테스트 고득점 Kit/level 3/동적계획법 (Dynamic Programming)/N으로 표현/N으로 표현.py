def solution(N, number):
    
    if N == number: return 1
    
    s = [ set() for x in range(8)]
    
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i) )
    
    '''
    n 일반화
    {
        "n" * i U
        1번 set 사칙연산 n-1번 set U
        2번 set 사칙연산 n-2번 set U
        ...
        n-1번 set 사칙연산 1번 set
    }
    '''
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]: # j+1번 세트 사칙연산
                for op2 in s[i-j-1]: # i-j번 세트 사칙연산.
                    # (j+1) + (i-j) = i+1
                    # 즉, 아래 연산은 i+1번 사용하여 표현할 수 있는 수들.
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    
                    if op2 != 0:
                        s[i].add(op1 // op2)
        
        if number in s[i]:
            return i + 1
    
    return -1
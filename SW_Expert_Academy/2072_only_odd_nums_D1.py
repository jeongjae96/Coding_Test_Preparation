# source: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number_list = map(int, input().split())
    
    answer = 0
    
    for num in number_list:
        if num % 2 == 1:
            answer += num
    
    print(f'#{test_case} {answer}')
    # ///////////////////////////////////////////////////////////////////////////////////

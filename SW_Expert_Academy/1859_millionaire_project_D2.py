'''
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
'''

# 주어진 배열을 거꾸로 봐야 for문을 한 번만 돌려 시간 효율성을 지킬 수 있는 문제.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    days = int(input())
    price_list = list(map(int, input().split()))
    
    answer = 0
    
    price_list.reverse()
    
    higher_price = price_list[0]

    for price in price_list:
        if higher_price > price:
            answer += higher_price - price
        else:
            higher_price = price
    
    print(f'#{test_case} {answer}')
    # ///////////////////////////////////////////////////////////////////////////////////

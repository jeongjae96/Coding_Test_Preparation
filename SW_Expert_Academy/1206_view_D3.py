# source: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

# input 대체
import sys
sys.stdin = open("1206_input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    buildings = int(input())
    building_info = list(map(int, input().split()))

    answer = 0

    for i in range(buildings):
        if i == 0:
            max_val = max(building_info[:i+3])
            
            nbr_max_val = max(building_info[i+1:i+3])

        elif i == 1:
            max_val = max(building_info[i-1:i+3])
            
            nbr_building_info = [building_info[i-1]] + building_info[i+1:i+3]
            nbr_max_val = max(nbr_building_info)
            
        elif i == len(building_info) - 2:
            max_val = max(building_info[i-2:i+2])

            nbr_building_info = building_info[i-2:i] + [building_info[i+1]]
            nbr_max_val = max(nbr_building_info)

        elif i == len(building_info) - 1:
            max_val = max(building_info[i-2:i+1])
            
            nbr_max_val = max(building_info[i-2:i])
    
        else:
            max_val = max(building_info[i-2:i+3])

            nbr_building_info = building_info[i-2:i] + building_info[i+1:i+3]
            nbr_max_val = max(nbr_building_info)

        if building_info[i] == max_val:
            answer += max_val - nbr_max_val

    print(f'#{test_case} {answer}')
    # ///////////////////////////////////////////////////////////////////////////////////

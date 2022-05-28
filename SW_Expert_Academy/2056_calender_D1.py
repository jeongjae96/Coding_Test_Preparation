# source: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    date = input()

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if int(year) < 1 or int(month) < 1 or int(month) > 12 or int(day) < 1 or int(day) > 31:
        print(f'#{test_case} -1')
        continue

    if int(month) == 2:
        if int(day) > 28:
            print(f'#{test_case} -1')
            continue
    
    if int(month) in (4, 6, 9, 11):
        if int(day) > 30:
            print(f'#{test_case} -1')
            continue
        
    
    print(f'#{test_case} {year}/{month}/{day}')
    # ///////////////////////////////////////////////////////////////////////////////////

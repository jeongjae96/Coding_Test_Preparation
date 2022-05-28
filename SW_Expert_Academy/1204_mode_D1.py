# source: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    _ = input()

    score_list = list(map(int, input().split()))


    mode_score = -1
    mode_num = 0

    for i in range(100, -1, -1):
        if mode_num < score_list.count(i):
            mode_score = i
            mode_num = score_list.count(i)

    print(f'#{test_case} {mode_score}')
    # ///////////////////////////////////////////////////////////////////////////////////

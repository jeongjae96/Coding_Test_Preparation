# 참고: https://minnnne.tistory.com/91
# dict 정렬: https://ddolcat.tistory.com/677

def solution(n, results):
    
    # win: 1, lose: -1, NA: 0
    win_lose = [[0 for i in range(n)] for j in range(n)]
    
    # 대결 횟수를 세기 위한 dict
    cnt = dict()
    
    for r in results:
        winner = r[0] - 1
        loser = r[1] - 1
        
        win_lose[winner][loser] = 1
        win_lose[loser][winner] = -1
        
        if cnt.get(winner) == None:
            cnt[winner] = 1
        else:
            cnt[winner] += 1
            
        if cnt.get(loser) == None:
            cnt[loser] = 1
        else:
            cnt[loser] += 1
            
    # 대결 횟수 내림차순 정렬
    cnt = sorted(cnt.items(), key=lambda cnt : cnt[1], reverse=True)
    
    # 대결 횟수 많았던 순으로 win_lose 리스트 갱신
    for c in cnt:
        
        win = []
        lose = []
        
        for i, value in enumerate(win_lose[c[0]]):
            
            if value == -1:
                lose.append(i)
            elif value == 1:
                win.append(i)
            
            for w in win:
                for l in lose:
                    win_lose[w][l] = -1
                    win_lose[l][w] = 1
                    
    answer = n
    
    for row in win_lose:
        count = 0
        
        for item in row:
            if item ==0: count +=1
            
            # item이 0인 횟수가 1을 넘는다면, 순위를 알 수 없다는 뜻이므로 answer에서 -1해준다.
            if count > 1:
                answer -= 1
                break
    
    return answer
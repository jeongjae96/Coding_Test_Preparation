# 참고: https://blog.naver.com/ameeam/222130179819
# 참고: https://it-garden.tistory.com/420

def solution(genres, plays):
    answer = []
    d = dict()
    
    for g, p in zip(genres, plays):
        if g in d.keys():
            d[g] += p
        else:
            d[g] = p
    
    d = sorted(d.items(), key=lambda x : x[1], reverse=True) # value 기준으로 정렬.
    
    for k, v in d:
        li = []
        for i, (g,p) in enumerate(zip(genres, plays)): # 속한 노래가 많이 재생된 장르부터
            if k == g:
                li.append([p,i])
                
        li = sorted(li, key=lambda x : (-x[0], x[1])) # 장르 내에서 많이 재생된 노래를 먼저 수록 -x[0]
        # 재생 횟수가 같을 시, 고유 번호가 낮은 노래를 먼저 수록 x[1]
        
        answer.append(li[0][1]) # 장르에 속한 곡이 하나라면, 하나의 곡만 선택.
        if len(li) > 1: # 장르 별로 가장 많이 재생된 노래 두 개씩 모아 출시.
            answer.append(li[1][1])
        
    return answer
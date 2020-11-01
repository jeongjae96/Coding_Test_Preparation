# 문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

# 참고: https://blog.naver.com/ujafratte111/221673689166
# 가로 * 세로 = 전체 타일의 수 (노랑 + 갈색 타일)
# (가로 - 2) * (세로 - 2) = 노랑 타일의 수

def solution(brown, yellow):

    total_tiles = brown + yellow
    
    for height in range(1, total_tiles+1):
        if total_tiles % height != 0:
            continue
        
        width =  total_tiles // height
        
        if (height - 2) * (width - 2) == yellow:
            return sorted([height, width], reverse = True) 
            # 제한사항 3: 가로 >= 세로
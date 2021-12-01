# N : 떡의 개수
# M : 요청한 떡의 길이
# 절단기에 설정할 수 있는 높이의 최댓값 출력

n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0

    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
        
    if total < m:
        end = mid - 1

    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)
'''
서로소 집합 알고리즘의 find 함수를 최적화하기 위해 경로 압축 기법 적용.
find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법.
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
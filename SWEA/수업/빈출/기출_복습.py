import sys
sys.stdin = open('기출.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    map = []
    for i in range(n):
        map.append(list(input()))   # H -> X 로 수정해야하므로 수정가능한 list로 받기 str 은 수정못함
    for s in map:
        print(s)
    print('--------------')

        # 1. 불러온 행렬을 탐색하면서 범위 안에 있는 H를 X로 바꿔야한다.
    type = {'A': 2, 'B': 3, 'C': 4}
    for r in range(n):
        for c in range(n):
            if map[r][c] == 'A' or map[r][c] == 'B' or map[r][c] == 'C':
                for k in range(1, type[map[r][c]]):
                    if c + k < n and map[r][c+k] == 'H': # 우
                        map[r][c+k] = 'X'
                    if c - k >= 0 and map[r][c-k] == 'H': # 좌
                        map[r][c-k] = 'X'
                    if r+k < n and map[r+k][c] == 'H': # 상
                        map[r+k][c] = 'X'
                    if r-k >= 0 and map [r-k][c] == 'H': # 하
                        map[r-k][c] = 'X'

    cnt = 0
    for r in range(n):
        for c in range(n):
            if map[r][c] == 'H':
                cnt += 1

    for s in map:
        print(s)
    print(cnt)




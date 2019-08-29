import sys
sys.stdin = open('폭탄2.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    max_sum = 0
    for r in range(n):
        for c in range(n):
            sum = 0

            # 좌상단
            x, y = r-1, c-1
            while 0 <= x < n and 0 <= y < n:   # x, y가 이 범위에서 벗어나면 종료.
                sum += arr[x][y]
                x, y = x-1, y-1

            # 우하단
            x, y = r+1, c+1
            while 0 <= x < n and 0 <= y < n:
                sum += arr[x][y]
                x, y = x+1, y+1

            # 좌하단
            x, y = r+1, c-1
            while 0 <= x < n and 0 <= y < n:
                sum += arr[x][y]
                x, y = x+1, y-1

            # 우상단
            x, y = r-1, c+1
            while 0 <= x < n and 0 <= y < n:
                sum += arr[x][y]
                x, y = x-1, y+1

            sum += arr[r][c]
            if sum >= max_sum:
                max_sum = sum
                a, b = r, c
    print(tc, a, b, max_sum)




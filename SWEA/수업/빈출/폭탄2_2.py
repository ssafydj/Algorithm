import sys
sys.stdin = open('폭탄2.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    # 4 7 11 1시 방향 대각 이동 (좌우 이동x)
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    a = b = max_sum = 0

    for r in range(n):
        for c in range(n):
            sum = 0
            for i in range(4):
                x, y = r + dx[i], c + dy[i]
                while 0 <= x < n and 0 <= y < n:
                    sum += arr[x][y]
                    x, y = x + dx[i], y + dy[i]
            sum += arr[r][c]
            if sum >= max_sum:
                max_sum = sum
                a = r
                b = c
    print(tc, a, b, max_sum)

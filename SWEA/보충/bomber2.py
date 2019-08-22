import sys
sys.stdin = open('99 Bomber_bomber2_input', 'r')
tc = int(input())
# print(tc)

for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = a = b = 0
    for r in range(N):
        for c in range(N):
            S = 0

        ## (0, 0) 기준으로 우하단의 인덱스는 (1, 1) 로 증가, 좌상단의 인덱스는 (-1, -1) 로 감소

            # 좌상단
            x, y = r - 1, c - 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x - 1, y - 1

            # 우상단
            x, y = r - 1, c + 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x - 1, y + 1

            # 좌하단
            x, y = r + 1, c - 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x + 1, y - 1

            # 우하단
            x, y = r + 1, c + 1
            while x >= 0 and x < N and y >= 0 and y < N:
                S += arr[x][y]
                x, y = x + 1, y + 1
            S += arr[r][c]
            if S >= ans:
                ans, a, b = S, r, c
        print('#{}'. format(tc), a, b, ans)






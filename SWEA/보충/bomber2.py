# import sys
# sys.stdin = open('99 Bomber_bomber2_input', 'r')
# tc = int(input())
# # print(tc)
#
# for t in range(1, tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = a = b = 0
#     for r in range(N):
#         for c in range(N):
#             S = 0
#
#         ## (0, 0) 기준으로 우하단의 인덱스는 (1, 1) 로 증가, 좌상단의 인덱스는 (-1, -1) 로 감소
#
#             # 좌상단
#             x, y = r - 1, c - 1
#             while x >= 0 and x < N and y >= 0 and y < N:
#                 S += arr[x][y]
#                 x, y = x - 1, y - 1
#
#             # 우상단
#             x, y = r - 1, c + 1
#             while x >= 0 and x < N and y >= 0 and y < N:
#                 S += arr[x][y]
#                 x, y = x - 1, y + 1
#
#             # 좌하단
#             x, y = r + 1, c - 1
#             while x >= 0 and x < N and y >= 0 and y < N:
#                 S += arr[x][y]
#                 x, y = x + 1, y - 1
#
#             # 우하단
#             x, y = r + 1, c + 1
#             while x >= 0 and x < N and y >= 0 and y < N:
#                 S += arr[x][y]
#                 x, y = x + 1, y + 1
#
#             S += arr[r][c]
#         print('#{}'. format(tc), a, b, ans)
#         if S >= ans:
#             ans, a, b = S, r, c

# ###########################################

import sys;

sys.stdin = open('bomber2_input.txt', 'r')
​
T = int(input())
​
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # x=행, y=열
    dx = [-1, -1, 1, 1]  # 좌상단, 우상단, 좌하단, 우하단
    dy = [-1, 1, -1, 1]
    answer = a = b = 0  # 최대값 저장
​
for r in range(N):
    for c in range(N):
        # 네 방향에 대해서 자료를 읽는다.
        S = 0
        for i in range(4):  # 좌상단, 우상단, 좌하단, 우하단
            x, y = r + dx[i], c + dy[i]
            # X 모양처럼 대각선모양에서 가운데 중점은 뒤로 미루고 좌상단, 우상단, 좌하단, 우하단 먼저 구하기
            # 위의 dx, dy값을 이용하면 가운데 값만 빼고 다 구할 수 있다.

            # while x >= 0 and x < N and y >= 0 and y < N: # 범위를 벗어나지 않을때까지
            while 0 <= x < N and 0 <= y < N:
                S += arr[x][y]
                x, y = x + dx[i], y + dy[i]
        S += arr[r][c]  # 중점을 더해주지 않았기 때문에 가운데 값이 비어있으니 한 번 넣어준다.
        if S >= answer:
            answer, a, b, = S, r, c

print('#{}'.format(tc), a, b, answer)




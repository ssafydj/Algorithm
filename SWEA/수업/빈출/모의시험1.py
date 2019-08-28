import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    # print(n, m, k)
    arr = [[0] * m for _ in range(n)]


    for i in range(k): # k = 사각 영역의 갯수
        x1, y1, x2, y2, color = map(int, input().split())
    # print(x1, y1, x2, y2, color)

        # 색칠을 할 수 있는지 판단
        draw = True # do!
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if arr[x][y] > color:       # 새로운 명도가 기존 보다 큰 경우에만 덮어쓸 수 있다.
                    draw = False # don't!
        # 색칠하기
        if draw == True:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    arr[x][y] = color

        # 각 명도의 갯수 구하기
        cnt = [0] * 11      # 명도 0~10 까지 11개 넣을 공간
        for x in range(n):
            for y in range(m):
                cnt[arr[x][y]] += 1
    print(max(cnt))



#################################

# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# tc = int(input())
# # print(tc)
#
#
#
# for i in range(1, tc+1):
#     n, m, k = list(map(int, input().split()))
#     arr = [[0] * 100 for _ in range(100)]
#     # print(n, m, k)
#
#     for j in range(k):
#         r1, c1, r2, c2, color = map(int, input().split())
#     # print(r1, c1, r2, c2, color)
#
#
#     for r in range(r1, r2+1):
#         for c in range(c1, c2+1):
#             arr[r][c] += color
#             if arr[r][c] > color:
#                 pass
#             else:
#                 arr[r][c] = color
#
#
#             arr_list = []
#             for row in range(100):
#                 for column in range(100):
#                     arr_list[arr[row][column]] = arr_list[arr[row][column]] + 1
#                 result = max(arr_list[arr[row][column]])
#
#     print('#{} {}'.format(i,result))


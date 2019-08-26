import sys
sys.stdin = open('4836.txt', 'r')

# tc = int(input())
#
# for _ in range(1, tc+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     # print(n)
#     print(arr)

    # for r in range(n):




test_case = int(input())

for i in range(test_case):
    givens = [[0] * 10 for i in range(10)]
    cnt = 0
    colors = int(input())
    for j in range(colors):
        r1, c1, r2, c2, color_num = map(int, input().split())
    # print(r1, c1, r2, c2, color_num)

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            givens[r][c] += color_num

            for column in range(10):
                for row in range(10):
                    if givens[column][row] == 3:
                        cnt += 1
    print(cnt)













#
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 givens[r][c] += color_num
#
#         for c_lengths in range(10):
#             for r_lengths in range(10):
#                 if givens[c_lengths][r_lengths] == 3:
#                     cnt += 1
#     print('#{0} {1}'.format(i + 1, cnt))

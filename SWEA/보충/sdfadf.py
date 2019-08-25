# import sys
# sys.stdin  = open('input (7).txt', 'r')
#
# tc = int(input())
# for t in range(1, tc + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr)
#
#     # 행 우선 순회
#
#     # 모든 자료의 합 구하기
#     total = 0
#     row_sum = col_sum = 0
#     for i in range(N): # 0~n-1 까지
#         row_sum = 0    # 새로운 행에 들어갈 때 마다 '초기화'(행 마다 값을 구하기 위해서)
#         col_sum = 0
#         for j in range(N):  # 0~n-1까지
#             row_sum += arr[i][j]  # 행우선
#             col_sum += arr[j][i]  # 열우선
#     print(row_sum, col_sum)
#

arr = [[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]

N, M = 5, 3

sum = 0
max_sum=0
for i in range(N-M+1):
    for j in range(N-M+1):
        sum = 0
        for r in range(i, i+M):
            for c in range(j, j+M):
                sum += arr[r][c]
                if sum > max_sum:
                    max_sum = sum
print(max_sum)
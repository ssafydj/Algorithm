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
#         print(row_sum, col_sum)
#
#
#     # 행과 열의 합에 최소값 구하기
#     ans = 99999999999   # 아무 큰 수나 두기 <-> 최대값 구할 때는 ans = 0 으로 설정
#     row_sum = col_sum = 0
#     for i in range(N):
#         row_sum = col_sum = 0
#         for j in range(N):
#             row_sum += arr[i][j]
#             col_sum += arr[j][i]
#         ans = min(ans, row_sum, col_sum)
#     print(ans)
#
#     # 대각 처리
#     dir = 0
#     for i in range(N):  #좌상단 -> 우하단
#         dir += arr[i][i]
#     ans = min(ans, S)
#     S = 0 # ans로 최소값 비교 했으므로 사용끝 -> 초기화에서 다음꺼에 사용
#
#     for i in range(N):  # 우상단 -> 좌하단
#         dir += arr[i][N-1-i]
#     ans = min(ans, S)

    # 사각 영역 탐색

tc = int(input())
for t in range(1, tc + 1):
    N, M = map(int(input()))
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 모든 M * M 영역의 좌상단 좌표를 만든다.
    for i in range(N-M+1):
        for j in range(N-M+1):

        # 좌상단 i, j, 가로세로 길이 = M 인 사각영역을 행우선으로 탐색
            for r in range(i, i+M):  # i ~ i+M-1 까지
                for c in range(j, j+m): # j~j+m-1 까지
                    arr[r][c]

#



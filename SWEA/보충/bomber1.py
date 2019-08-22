import sys
sys.stdin = open('01.IM_보충수업_01.배열탐색_bomber1_input.txt', 'r')
tc = int(input())
# print(tc)

for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_sum = x= y= 0 # 최대값 저장 및 행과 열 번호
    for r in range(N):
        for c in range(N):
            sum = 0
            for i in range(N):
                sum += arr[r][i] + arr[i][c]
            sum -= arr[r][c]        # 5*5 에서 겹치는 1부분 제외
            if sum >= max_sum:
                max_sum, r ,c = sum, x, y
    print(max_sum, r, c)

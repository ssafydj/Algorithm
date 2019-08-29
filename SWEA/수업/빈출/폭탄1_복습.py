import sys
sys.stdin = open('폭격1.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    max_sum = 0
    # 1. 전체 돌아야하는 범위
    for i in range(n):
        for j in range(n):
            sum = 0
    # 2. 더할 행과 열의 값
            for k in range(n):
                sum += arr[i][k] + arr[k][j]
    # 3. 행과 열의 겹치는 부분
            sum -= arr[i][j]
            if sum >= max_sum:
                max_sum = sum
                x = i
                y = j
    print(x, y, max_sum)
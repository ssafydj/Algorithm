import sys
sys.stdin = open('bomber1_input.txt', 'r')

tc = int(input())
# print(tc)
#
for _ in range(1, tc +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    max_sum = 0
    x = y = 0

    for r in range(n):
        for c in range(n):
            sum = 0
            for i in range(n):
                sum += arr[r][i] + arr[i][c]
            sum -= arr[r][c]
            if sum >= max_sum:
                max_sum, x, y = sum, r, c
    print(x, y, max_sum)
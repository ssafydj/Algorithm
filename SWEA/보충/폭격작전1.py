import sys
sys.stdin = open('bomber3_input.txt', 'r')

tc = int(input())

for _ in range(1, tc +1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split()))for _ in range(n)]
    # print(n, m)
    # print(arr)

    max_sum = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    sum += arr[r][c]
                if sum >= max_sum:
                    max_sum = sum
                    x = r
                    y = c
    print(x, y, max_sum)
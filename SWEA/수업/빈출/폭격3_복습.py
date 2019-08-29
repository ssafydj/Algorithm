import sys
sys.stdin = open('bomber3.txt', 'r')

t = int(input())
print(t)

for tc in range(1, t+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n, m)
    # print(arr)

    sum_max = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    sum += arr[r][c]
                    if sum_max <= sum:
                        sum_max = sum
                        x = i
                        y = j
    print('#{} {} {} {}'.format(tc, x, y, sum_max))

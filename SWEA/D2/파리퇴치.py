import sys
sys.stdin = open('2001.txt', 'r')
tc = int(input())

for t in range(1, tc+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n, m)
    # print(arr)

    sum = 0
    max_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    sum += arr[r][c]
                    if sum >= max_sum:
                        max_sum = sum
    print('#{} {}'.format(t , max_sum))



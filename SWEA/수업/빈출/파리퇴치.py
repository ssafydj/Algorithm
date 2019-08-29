import sys
sys.stdin = open('파리퇴치.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n, m)
    # print(arr)

    max_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    sum += arr[r][c]
                    if max_sum < sum:
                        max_sum = sum
    print('#{} {}'.format(tc, max_sum))


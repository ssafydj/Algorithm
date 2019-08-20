import sys
sys.stdin = open('bomber3.txt', 'r')

tc = int(input())
# print(tc)
for t in range(tc+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    sum = 0
    max_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    sum += arr[r][c]
                if max_sum <= sum:
                    max_sum = sum

    print('#{} {} {} {}'.format(t+1 ,i, j, max_sum))



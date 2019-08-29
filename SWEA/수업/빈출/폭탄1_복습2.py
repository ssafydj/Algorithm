import sys
sys.stdin = open('폭격1.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    max_sum = 0
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += arr[i][k] + arr[k][j]
            sum -= arr[i][j]
            if max_sum < sum:
                max_sum = sum
    print(max_sum)

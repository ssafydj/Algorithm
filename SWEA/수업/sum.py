import sys
sys.stdin = open('sum.txt', 'r')

for tc in range(1, 11):
    n = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(100)]

    # print(arr)


    max_sum = 0

    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += arr[i][j]
        max_sum = max(max_sum, sum1)
    # print(max_sum)


    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += arr[j][i]
        max_sum = max(max_sum, sum1)

    sum1 = 0
    for i in range(100):
        sum1 += arr[i][i]
    max_sum = max(max_sum, sum1)

    sum1 = 0
    for i in range(100):
        sum1 += arr[i][99-i]
    max_sum = max(max_sum, sum1)

    print('#{} {}'.format(tc, max_sum))
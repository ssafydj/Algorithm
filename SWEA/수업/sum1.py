import sys
sys.stdin = open('sum.txt', 'r')

for tc in range(1, 11):
    n = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(n)
    # print(arr)

    max_sum = 0

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        max_sum = max(max_sum, sum)

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        max_sum = max(max_sum, sum)

    sum = 0
    for i in range(100):
        sum += arr[i][i]
        max_sum = max(max_sum, sum)

    sum = 0
    for i in range(100):
        sum += arr[i][99-i]
        max_sum = max(max_sum, sum)

    print(max_sum)





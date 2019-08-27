import sys
sys.stdin = open('부분집합.txt', 'r')

tc = int(input())

for v in range(1, tc+1):
    n, k = list(map(int, input().split()))
    # print(n, k)

    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum == k:
            result = 1
        else:
            result = 0

    print('#{} {}'.format(v, result))

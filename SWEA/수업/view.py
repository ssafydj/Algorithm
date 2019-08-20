import sys
sys.stdin = open('view.txt', 'r')

for k in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(n)
    # print(arr)
    result = 0
    for j in range(2, n-2):
        Max = max(arr[j-2], arr[j-1], arr[j+1], arr[j+2])
        if arr[j]> Max:
            result += arr[j] - Max
    print('#{} {}'.format(k+1, result))



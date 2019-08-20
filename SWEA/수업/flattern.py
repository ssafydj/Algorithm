import sys
sys.stdin = open('flattern.txt', 'r')

for _ in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(n)
    # print(arr)
    # print(len(arr))

    for count in range(n):
        Max = 0
        Min = 0
        for i in range(1, len(arr)):
            if arr[Min] > arr[i]:
                Min = i
            if arr[Max] < arr[i]:
                Max = i

        if count == n:
            break
        else:
            arr[Min] += 1
            arr[Max] -= 1
        result = arr[Max] - arr[Min]
    print(result)





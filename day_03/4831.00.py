T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) +[N]

    ans = bus = 0

    for i in range(1, M + 2):
        if arr[i] - arr[i - 1] > K:
            ans = 0
            break
        if arr[i] > bus + K:
            bus = arr[i - 1]
            ans += 1
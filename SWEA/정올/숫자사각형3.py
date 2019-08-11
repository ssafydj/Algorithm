N = int(input())

arr = [[0] * N for _ in range(N)]

NUM = 1
for i in range(N):
    for j in range(N):
        arr[j][i] = NUM
        NUM += 1

cnt = 0
for j in range(N):
    for i in range(N):
        print(arr[j][i], end=' ')
        cnt += 1
        if cnt == N:
            cnt = 0
            print()
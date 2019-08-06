N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

NUM = 1
for i in range(N):
    for j in range(M):
        arr[i][j] = NUM
        NUM += 1
cnt = 0
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
        cnt+=1
        if cnt ==N:
            cnt = 0
            print()


N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

num = 1
for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            arr[i][j] = num
            num += 1
    else:
        for j in range(M - 1, -1, -1):
            arr[i][j] = num
            num += 1
    
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
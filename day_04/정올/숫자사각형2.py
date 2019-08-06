N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

NUM = 0
for i in range(N):
    for j in range(M):
        if i % 2 == 0:      #행 = 짝수
            NUM += 1
            arr[i][j] = NUM
        else:               #행 = 홀수
            NUM += 1
            arr[i][N - j] = NUM
print(arr)

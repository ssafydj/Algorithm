# n, m = map(int(input().split()))

# arr = [[0] * m for _ in range(n)]

# num = 1
# for i in range(n):
#     for j in range(m):
#         arr[i][j] = num
#         num += 1



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


        

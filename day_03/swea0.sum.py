import sys
sys.stdin = open("input (1).txt", "r")

T = int(input())
arr = [list(map(int, input().split())) for i in range(100)]
print(T, arr)

N, M = len(arr), len(arr[0])

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    

for i in range(N):
    for j in range(M):
        print(arr[j][i], end=' ')


for diag in range(0, N + M -1):

    x = 0 if diag < M else (diag - M + 1)
    y = diag if diag < M else M - 1

    while x < N and y >= 0:
        print(arr[x][y], end='')
        x += 1
        y -= 1

for reverse in range(N + M -1, 0, -1):




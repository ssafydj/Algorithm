import sys
sys.stdin = open("input (1).txt", "r")

T = int(input())
arr = [list(map(int, input().split())) for i in range(100)]
print(T, arr)
N, M = len(arr), len(arr[0])
MAX = 0

for i in range(N):
    SUM = 0
    for j in range(M):
        SUM += arr[i][j]
    MAX = max(SUM, MAX)
# print(MAX)

for i in range(N):
    SUM = 0
    for j in range(M):
        SUM += arr[j][i]
    MAX = max(SUM, MAX)
# print(MAX)

SUM = 0
for i in range(N):
    SUM += arr[i][i]
    MAX = max(SUM, MAX)
# print(MAX)

SUM = 0
for i in range(N):
    SUM += arr[i][N - 1]
    MAX = max(SUM, MAX)
# print(MAX)

print('#{}'.format(MAX))

arr = [0]*50
n, m = list(map(int, input().split()))

for i in range(n):
    row_sum = col_sum = 0
    for j in range(m):
        row_sum += arr[i][j]
        col_sum += arr[j][i]


####################################

arr = 99999999999
row_sum = col_sum = 0

for i in range(n):
    row_sum = col_sum = 0
    for j in range(m):
        row_sum += arr[i][j]
        col_sum += arr[j][i]
    arr = min(arr, row_sum, col_sum)

###############################
arr = [[ 1,  2,  3,  4,  5],
       [10,  9,  8,  7,  6],
       [11, 12, 13, 14, 15],
       [20, 19, 18, 17, 16],
       [21, 22, 23, 24, 25]]
N, M = len(arr), len(arr[0])

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(arr[i][j], end='')
    else:
        for j in range(N -1, -1, -1):
            print(arr[i][j], end='')
        print()

arr = [[ 1,  2,  3,  4,  5],
       [10,  9,  8,  7,  6],
       [11, 12, 13, 14, 15],
       [20, 19, 18, 17, 16],
       [21, 22, 23, 24, 25]]

N, M = len(arr), len(arr[0])
for i in range(N):
    if i & 1 == 0:              # 짝수
        for j in range(M):
            print('%2d ' % arr[i][j], end='')
    else:
        for j in range(M - 1, -1, -1):
            print('%2d ' % arr[i][j], end='')
    print()

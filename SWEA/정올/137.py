n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
num = 1
for row in range(n):
    for column in range(m):
        arr[row][column] = num
print(num)

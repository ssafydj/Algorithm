n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print((i+1)*(j+1), end=' ')
    print()

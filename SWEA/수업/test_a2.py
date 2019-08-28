import sys
sys.stdin = open('test_a2.txt', 'r')

tc = int(input())

for i in range(1, tc+1):
    n = int(input())
    arr = [[0] * 2000 for _ in range(2000)]
    for j in range(n):
        x, y ,d, k = list(map(str, input().split()))
    #     print(x, y ,d, k)
    # print('-----')
        sum = 0
        for r in range(n):
            if x[r] == x[r+1] and y[r] != y[r+1] and d == 0:
                sum += k
            elif x[r] == x[r+1] and y[r] != y[r+1] and d == 1:
                sum += k
            elif x[r] != x[r+1] and y[r] == y[r+1] and d == 0:
                sum += k
            elif x[r] != x[r + 1] and y[r] == y[r + 1] and d == 1:
                sum += k
            elif x[r] == x[r+1] and y[r] != y[r+1] and d == 2:
                sum += k
            elif x[r] == x[r+1] and y[r] != y[r+1] and d == 3:
                sum += k
            elif x[r] != x[r+1] and y[r] == y[r+1] and d == 2:
                sum += k
            elif x[r] != x[r + 1] and y[r] == y[r + 1] and d == 3:
                sum += k
    print(sum)




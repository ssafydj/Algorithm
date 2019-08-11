import sys
sys.stdin = open("2029.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n, m = map(int, input().split())
    # print(n, m)

    i = n // m 
    j = n % m 


    print('#{} {} {}'.format(k, i, j))

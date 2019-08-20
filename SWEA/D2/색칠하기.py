import sys
sys.stdin = open('4836.txt', 'r')
tc = int(input())

for t in range(1, tc+1):
    n, m = list(map(int, input().split()))
    # print(n)
    # print(m)
    for i in range(n - m + 1):
        for j in range(n - m + 1):


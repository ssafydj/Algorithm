import sys
sys.stdin = open("2056.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n = list(map(int, input().split()))
    print(n)

    
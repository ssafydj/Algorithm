import sys
sys.stdin = open("2071.txt", "r")

tc = int(input())
for k in range(tc + 1):
    n = map(int, input().split())
print(n)
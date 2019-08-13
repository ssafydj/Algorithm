import sys
sys.stdin = open("1983.txt", "r")

tc = int(input())

for i in range(1, tc + 1):
    num = list(map(int, input().split()))
    print(num)
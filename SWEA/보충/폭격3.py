import sys
sys.stdin = open('폭격3.txt', 'r')

t = int(input())
# print(t)

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(m):


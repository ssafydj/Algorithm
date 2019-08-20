import sys
sys.stdin = open('01.IM_보충수업_01.배열탐색_bomber1_input.txt', 'r')
tc = int(input())
# print(tc)

for t in range(1, tc+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)
    for i in range(n):
        for

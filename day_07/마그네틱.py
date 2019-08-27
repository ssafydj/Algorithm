import sys
sys.stdin = open('1220.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a = 0 # 1과 2가 교차하는 누적합

    for i in range(n):
        c = 0
        for j in range(n):
            if arr[j][i] == 1:
                c = 1
            if arr[j][i] == 2 and c == 1:
                c = 0
                a += 1
    print('#{} {}'.format(tc, a))
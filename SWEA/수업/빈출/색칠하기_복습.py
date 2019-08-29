import sys
sys.stdin = open('색칠하기.txt', 'r')

t = int(input())

# 1. 각 변수를 불러오기
for tc in range(1, t+1):
    n = int(input())
    # print(n)
    arr = [[0] * 10 for _ in range(10)]
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)

# 2. 칸 별로 숫자 주기
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    # 3. 숫자의 크기가 1+2 = 3 인 경우 계산하기
    cnt = 0
    for row in range(r1, r2+1):
        for column in range(c1, c2+1):
            if arr[row][column] == 3:
                cnt += 1
    print(cnt)


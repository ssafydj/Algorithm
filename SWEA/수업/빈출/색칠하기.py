import sys
sys.stdin = open('색칠하기.txt', 'r')

tc = int(input())

for i in range(1, tc+1):
    cnt = 0
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]     # 2. 아래에 받은 변수를 공간에 할당하기 위해 여유있는 arr
    for j in range(n):
        r1, c1, r2, c2, color = map(int, input().split()) # 1. 각 변수가 필요하므로 각자 받기
        # print(r1, c1, r2, c2, color)

        for r in range(r1, r2+1): # 가로 길이
            for c in range(c1, c2+1): # 세로 길이
                arr[r][c] += color  # 각 좌표에 색(1 or 2)기입

                for row in range(10):    # 위에 만든 arr에
                    for column in range(10):
                        if arr[row][column] == 3:   # 각 좌표에 색이 3(1+2)인 좌표 구하기
                            cnt += 1
                            arr[r][c] = 0
    print('#{} {}'.format(i, cnt))

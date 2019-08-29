import sys
sys.stdin = open('sample_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    for i in range(k): # k = 색칠할 상자의 갯수
        x1, y1, x2, y2, color = map(int, input().split())
        # print(x1, y1, x2, y2, color)

        # 1. 색칠할 수 있는지 판단
        draw = True # 일단 모두 그리는 걸로 설정하고
        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                if arr[r][c] > color:
                    draw = False    # 특정 경우에만 그리지 않는걸로
        # 2. 색칠하기
        if draw:
            for r in range(x1, x2 + 1):
                for c in range(y1, y2 + 1):
                    arr[r][c] = color
        # 3. 명도별로 카운트 세기
        cnt = [0] * 11
        for r in range(n):
            for c in range(m):
                cnt[arr[r][c]] += 1
    print(max(cnt))

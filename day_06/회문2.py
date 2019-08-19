

for idx in range(100):
    for x in range(100):
        # 길이가 짝수인 경우에는 x -> l(왼쪽)
        l, r, cnt = x, x + 1, 0
        while l >= 0 and r < 100
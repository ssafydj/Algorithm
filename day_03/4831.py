


station = [0] * (N+1)

count = 0       # 충전 횟수
position = 0     # 현재위치

for i in arr:
    station[i] = 1

while position < N:
    for i in range(K+position, position, -1): # 뒤에서 앞으로 -1씩 체크
        if station[i]:
            count += 1
            position = i
            break
    else:
        count = 0
        break
    if (position +K) >= N:
        break

print('#{} {}'.format(test_case, count))
    
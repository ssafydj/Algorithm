for p in range(T):
    k, n, m = list(map(int, input.split())
    m_list = list(map(int, input().split()))

    loc = charge = fail = move = 0
    현재위치/충전횟수/충전소없어서 못가능경우/ 충전소-loc

    while loc < (n-k) and fail == 0:
        for j in range(k, 0, -1):
            if (loc +j bot in m_list:
                fail = 1
            else:
                fail = 0
                move = j
                loc += move
                charge += 1
                break
    
    if fail == 1:
        charge = 0

print('#{} {}'.format(p+1, charge))
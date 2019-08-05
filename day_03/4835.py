T = int(input())
for k in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))

for i in range(M):
    MAX += n_list[i]
    MIN += n_list[i]
    MAX = MIN = SUM

for i in range(1, N-M+1)):  # i는 구간의 시작위치
    crt = 0
    for j in range(i, i+M):
        crt += n_list[j]
        
    if MAX < crt:
        MAX = crt
    if MIN > crt:
        MIN = crt

    print( '#{} {}'.format(k+1, MAX-MIN))



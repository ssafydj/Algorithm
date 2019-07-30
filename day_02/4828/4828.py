import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())                     
    ai = list(map(int, input().split()))

    MAX = ai[0]
    MIN = ai[0]
    for j in range(1, len(ai)):
        if MAX < ai[j]:
            MAX = ai[j]        
        if MIN > ai[j]:
            MIN = ai[j]

    result = MAX - MIN
    print('#{} {}'.format(i+1, result))


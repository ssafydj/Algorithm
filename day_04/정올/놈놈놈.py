import sys
sys.stdin = open("2070.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n, m = list(map(int, input().split()))
    # print(n, m)

    if n < m:
        print('#{} {}'.format(k, '<'))
    elif n == m:
        print('#{} {}'.format(k, '='))
    else:
        print('#{} {}'.format(k, '>'))
    
    # 아래에 한 번에 print 할 경우에는 3가지 case를 표현 못하므로 각 케이스에 print를 넣어서 표현
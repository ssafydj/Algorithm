import sys
sys.stdin = open('이진탐색.txt', 'r')

tc = int(input())

for v in range(1, tc+1):
    p, pa, pb = list(map(int, input().split()))
    # print(p, pa, pb)

    cnt_a = 0
    left = 1
    while p == pa:
        pa = left = int((left + p) // 2)
        cnt_a += 1
    print(cnt_a)

    # cnt_b = 0
    # left = 1
    # while p == pb:
    #     left = int((left + p) // 2)
    #     cnt_b += 1
    #
    #     result = ''
    #     if cnt_a > cnt_b:
    #         result = A
    #     elif cnt_a == cnt_b:
    #         result = '0'
    #     else:
    #         result = B
    #
    # print('#{} {}'.format(v, result))

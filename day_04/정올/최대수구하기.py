import sys
sys.stdin = open("2068.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n = list(map(int, input().split()))
    # print(n)

    Max = n[0]
    # print(Max)

    for i in range(1, 10):
        if n[i] > Max:
            Max = n[i]
    # print(Max)
    print('#{} {}'.format(k , Max))


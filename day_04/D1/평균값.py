import sys
sys.stdin = open("2071.txt", "r")


tc = int(input())
for k in range(1, tc + 1):
    n = list(map(int, input().split()))
# print(n)
    zero = 0
    for i in n:
        zero += i
        result = zero / len(n)
    # print(round(result))

    print('#{} {}'.format(k, round(result)))
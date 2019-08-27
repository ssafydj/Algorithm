import sys
sys.stdin = open('문자열비교.txt', 'r')

tc = int(input())

for v in range(1, tc+1):
    n = input()
    m = input()

    for i in m:
        if n[::] in m[::]:
            result = 1
        else:
            result = 0
    print('#{} {}'.format(v, result))
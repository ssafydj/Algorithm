import sys
sys.stdin = open('정곤이.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = map(int, input().split())
    max_num =-1

    for i in range(n-1):
        for j in range(i+1, n):
            s = li[i] * li[j]
            t = s
            while t != 0:
                a = t % 10  # 1의 자리수
                t = t // 10     # 1의 자리수를 제외한 나머지 수
                b = t & 10
                if b > a:
                    break
            if t == 0:
                if max_num < s:
                    max_num = s

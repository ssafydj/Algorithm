import sys
sys.stdin = open('구간합.txt', 'r')
tc = int(input())

for v in range(1, tc+1):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    result = 0
    Max = 0
    Min = 999999
    ans_max = ans_min= 0


    for i in range(0, n-m+1):
        result = 0   # 초기화 -> 다음 반복에 지장없도록
        for j in range(i, i+m):
            result += arr[j]
        if Max < result:
            Max = result
        if Min > result:
            Min = result
        ans_max = max(Max, result)
        ans_min  = min(Min, result)
    print('#{} {}'.format(v, ans_max-ans_min))

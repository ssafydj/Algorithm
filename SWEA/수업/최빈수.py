import sys
sys.stdin = open('최빈수.txt', 'r')

tc = int(input())

for v in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)

    cnt = [0] * 101 # 0~100 까지 각 점수별로 공간 제공
    for score in arr:
        cnt[score] += 1
    # print(cnt)

    maxidx = 0
    for i in range(1, 101):
        if cnt[maxidx] <= cnt[i]:
            maxidx = i
    print(maxidx)







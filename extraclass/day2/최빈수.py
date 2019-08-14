import sys
sys.stdin = open("1204.txt", "r")

tc = int(input())
# print(tc)

for k in range(1, tc + 1):           # 1~t까지 나중에 출력에 사용
    n = list(map(int, input().split())) # 1000개의 데이터
    # print(n)

#빈도수 계산
    cnt = [0] * 101  #0~100 점 사이의 점수가 입력되므로
    for score in n:
        cnt[score] = cnt[score] + 1    # 1000개의 데이터를 통해 0~100 점 의 빈도가 계산됨

#최대값(빈도수가 가장 많은) 의 위치(점수)를 찾아야 한다.
    MaxIdx = 0
    for i in range(1, 101):
        if arr[MaxIdx] <= arr[i]:    #<= 가장 뒤에 있는 빈도수가 많은 점수가 출력된다.
            MaxIdx = i
        print("#{} {}".format(tc, MaxIdx))
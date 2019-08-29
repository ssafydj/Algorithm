import sys
sys.stdin = open('마그네틱.txt', 'r')



for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    cnt = 0
    for i in range(n):
        c = 0   # i = 0 일 때, j의 반복이 끝나고 i = 1 을 시작할 때 정의된 c 가 필요
        for j in range(n):
            if arr[j][i] == 1:
                c = 1
            if arr[j][i] == 2 and c == 1:   # 이 조건이 충족 안되면, c = 0 이 아닌 c = 1 이므로
                cnt += 1                     # 새로운 행에 들어가기 전에 c = 0 으로 초기화가 필요함
                c = 0
    print(cnt)
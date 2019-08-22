import sys
sys.stdin = open('bomber3.txt', 'r')

tc = int(input())
# print(tc)
for t in range(tc+1):
    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(n)
    # print(arr)

    sum = 0
    max_sum = 0
    for i in range(n-m+1):      #n*n 행렬에서 m 크기의 상자가 갈수 있는 최대 좌표는 (n-m+1)*(n-m+1)
        for j in range(n-m+1):
            sum = 0
            for r in range(i, i+m):  # i = 0 일때 길이가 m까지 가려면 m-1개가 필요. 따라서 i+m 으로 입력
                for c in range(j, j+m):
                    sum += arr[r][c]
                if max_sum <= sum:
                    max_sum = sum
                    a = i
                    b = j       # 위의 조건이 만족했을 때, i와 j가 필요한것!

    print('#{} {} {} {}'.format(t+1 ,a, b, max_sum))



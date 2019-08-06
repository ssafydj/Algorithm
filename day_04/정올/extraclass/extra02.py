N = int(input())

arr = [[0] * N for _ in range(N)]

num = 1
for i in range(N):      
    for j in range(N):
        arr[j][i] = num
        num += 1

for j in range(N):      # 열 기준 정렬도 가로 방향으로 입력되므로 열 ->행 순으로 for 문이 돌아야함
    for i in range(N):
        print(arr[j][i], end=' ')
    print()

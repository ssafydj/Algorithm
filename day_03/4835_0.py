# 슬라이딩 윈도우: 배열의 연속적인 구간을 왼쪽에서 오른쪽으로
# 움직이면서 문제를 해결하는 방법

T = int(input())

for text_case in range(1, T+1)
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Sum = 0
for i in range(M):
    SUM += arr[i]

Min = Max + Sum
for i in range(N-M+1):
    Sum += (arr[i+M] - arr[i])
    Min = min(Min, Sum)
    Max = max(Max, Sum)

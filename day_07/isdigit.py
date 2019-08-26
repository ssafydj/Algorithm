import sys
sys.stdin = open('1220.txt', 'r')

tc = int(input())
# print(tc)

for _ in range(1, tc+1):
    n = list(map(int, input().split()))
    arr =list(map(int, input().split()))
    print(n)
    print(arr)

    # 열우선 탐색->1과 2가 위아래로 교착하는 구간의 갯수 찾기
    cnt = 0
    for r in range(100):
        for c in range(100):





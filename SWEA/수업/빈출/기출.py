import sys;

sys.stdin = open('기출.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    map = []
    for _ in range(N):
        map.append(list(input()))  # str으로 받으면 문자열 변경못하므로 list로 하나하나 쪼개서 받기
    for s in map:
        print(s)
    type = {'A': 2, 'B': 3, 'C': 4} # 1, 2, 3 이지만 range에서 반복하기 위해 +1 딕셔너리 value 값 접근!
    for i in range(N):
        for j in range(N):  # i: 행값, j:열값
            if map[i][j] != 'H' and map[i][j] != 'X':
                for k in range(1, type[map[i][j]]): # 딕셔너리 type의 value에 접근
                    if j + k < N and map[i][j + k] == 'H':  # 우
                        map[i][j + k] = 'X'
                    if j - k >= 0 and map[i][j - k] == 'H':  # 좌
                        map[i][j - k] = 'X'
                    if i + k < N and map[i + k][j] == 'H':  # 하
                        map[i + k][j] = 'X'
                    if i - k >= 0 and map[i - k][j] == 'H':  # 상
                        map[i - k][j] = 'X'
    ans = 0
    for i in range(N):
        for j in range(N):  # i: 행값, j:열값
            if map[i][j] == 'H':
                ans += 1
    print('#{} {}'.format(tc, ans))
    for s in map:
        print(s)

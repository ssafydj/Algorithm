#input 파일 필요


for tc in range(1, 11):
    N = int(input())      # N = 입력값(갯수)
    arr = [input() for _ in range(8)]
    ans = 0

    # 한 행에 대해서
    # 길이가 N인 문자열의 모든 시작 위치, 0 ~ 8 - N
    for idx in range():   # 아래의 한 행 X 전체 행 이므로 반복
        for start in range(8 - N + 1):
            end = start + N - 1
            for i in range(N//2):
                if arr[idx][start + i] != arr[idx][end - i]: break
                else:
                    ans += 1
    # 모든 열에 대해서 반복 = [idx][s + i] -> [s + i][idx]
            for i in range(N//2):
                if arr[start + i][idx] != arr[end - i][idx]: break
                else:
                    ans += 1
    print(ans)
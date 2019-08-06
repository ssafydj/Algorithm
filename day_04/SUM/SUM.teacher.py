import sys
sys.stdin = open("input (1).txt", "r")

for tc in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
                                            # 100행의 리스트이므로 100*100
    ans = 0  # 최대값 저장
    # 행의 합
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[i][j]
        ans = max(ans, S)
    
    # 열의 합
    for i in range(100):
        S = 0
        for j in range(100):
            S += arr[j][i]
        ans = max(ans, S)

    # 좌상단 -> 우하단
    S = 0
    for i in range(100):
        S += arr[i][i]
    ans = max(ans, S)

    # 우상단 -> 좌하단
    S = 0
    for i in range(100):
        S += arr[i][99 - i]
    ans = max(ans, S)
    
    print('#{} {}'.format(tc+0, ans))





# 합친거
# ans = 0
# dsum1 = dsum2 = 0
# for i in range(100): 
#     rsum = csum = 0
#     dsum1 += arr[i][j]
#     dsum2 += arr[i][99 - i]
#     for j in range(100):
#         rsum += arr[i][j]
#         csum += arr[j][i]
#     ans = max(ans, rsum, csum)
# ans = max(ans, dsum1, dsum2) 

# print(ans)
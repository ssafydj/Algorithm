import sys
sys.stdin = open("4861.txt", "r")

tc = int(input())
n, m = map(int, input().split())
for k in range(1, n + 1):
    arr = input()
    l = len(arr)
    # print(arr)
    
    for i in range(l//2):
        if arr[i] == arr[l-1-i]:
            result = arr
    print(result)
    
#######################################################################강사님 풀이

    arr = []
    N = M = 0  # N: 행의 길이 , M: 찾을 회문 길이
    # 시작위치 0 ~ N-M


    # 2) 모든 행에 적용
for row in range(N):

    # 1) 한 행에 대해서 적용
    for start in range(N-M+1):
        end = start + M -1
        for i in range(M//2):
            if arr[row][start + i] != arr[row][end - i]:     #행과 열을 같이 비교하는 방법
                break
            else:
                #회문을 찾음
    



# arr = [i for i in range(10)]
# N = len(arr)
                
# for i in range(N):
#     print(arr[i], end=' ')
                
# i = 0
# while i < N:
#     print(arr[i], end=' ')
#     i += 1






# tc = int(input())
# n , m = map(int, input().split())
# for k in range(1, n + 1):
#     for a in range(1, m + 1):
#     arr = input()
#     m = len(arr)
#     # print(arr)

#     for i in range(m//2):
#         if arr[i] == arr[m-1-i]:
#             result = arr
#     print(result)
    



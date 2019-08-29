import sys
sys.stdin = open('기출2.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    num = int(input())
    arr = list(map(int, input().split()))
    arr_room = [0] * num

    cnt = 0
    for i in range(num):
        if arr == arr_room:
            break
        else:
            if arr[i] != arr_room[i]:
                for j in range(i, num, i+1):
                    if arr_room[j] == 1:
                        arr_room[j] = 0
                    else:
                        arr_room[j] = 1
                cnt += 1
    print(cnt)












# # 인덱스를 나눠서 나머지가 0이면 바꿈
# for i in range(1, len(arr)+1):
#     if arr[i] % i ==0 and arr[i] == 0:
#         arr[i] == 1
#     elif arr[i] % i ==0 and arr[i] == 1:
#         arr[i] == 0

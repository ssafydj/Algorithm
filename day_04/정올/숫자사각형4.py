N = int(input())
arr = [[0] * N for _ in range(N)]

# cnt = 0
# NUM = 1
# for i in range(N):
#     for j in range(N):
#         arr[i][j] = NUM
#         print(arr[i][j], end=' ')
#         cnt += 1
#         if cnt == 5:
#             cnt = 0
#             NUM += 1
#             print()



# cnt = 0
# NUM = 1
# for i in range(N):
#     for j in range(N):
#         arr[i][j] = NUM
#         NUM += 1
#         print(arr[i][j], end='')
#         cnt += 1
#         if cnt == 5:
#             print()
#             NUM = 1
#             cnt = 0
           
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] = i*j
        print(arr[i][j], end=' ')
        cnt += 1
        if cnt == N:
            print()
            cnt = 0


        

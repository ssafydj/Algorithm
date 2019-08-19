# # 5*5 별 모양 정사각형
# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()


# 대각선 모양
for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    

# 계단 모양
for i in range(5):
    for j in range(5):
        if i >= j:
            print('*', end='')
        
    print()

   

arr= [
[4 ,4 ,3 ,2 ,1],
[2 ,2 ,1 ,6 ,5],
[3 ,5 ,4 ,6 ,7],
[4 ,2 ,5 ,9 ,7],
[8 ,1 ,9 ,5 ,6]
]

MAX = 0
# 행 단위 합 구하기
# for i in range(5):
#     SUM = 0
#     for j in range(5):
#         SUM += arr[i][j]
#     MAX = max(SUM, MAX)
# print(MAX)

# # 열 단위 합 구하기
# for i in range(5):
#     SUM = 0
#     for j in range(5):
#         SUM += arr[j][i]
#     MAX = max(SUM, MAX)
# print(MAX)

# # 대각 합 구하기
# SUM = 0
# for i in range(5):
#     SUM += arr[i][i]   
#     Max = max(SUM, MAX)

# # 역대각 합 구하기
# SUM = 0
# for i in range(5):
#     SUM += arr[i][4 - i]   
#     Max = max(SUM, MAX)
# arr = [
# [9, 20, 2, 18, 11],
# [19, 1, 25, 3, 21],
# [8, 24, 10, 17, 7],
# [15, 4, 16, 5, 6],
# [12, 13, 22, 23, 14]  
# ]

# N, M = len(arr), len(arr[0])

# dx = [0, 0, 1, -1]  #상하좌우 이동하는 좌표를 각각 리스트로 저장 > 좌표를 생성하기 위함 > 코드가 간결
# dy = [1, -1, 0, 0]

# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             tx, ty = x +dx[i], y +dy[i]

#         if tx <0 or tx == N or ty < 0 or ty == N: continue


arr='ABC'
bits = [0]*3

def print_set(bits):
    print(bits, end=' ')
    for i in range(len(bits)):
        if bits[i]:
            print(arr[i], end=' ')
    print()

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            print(print_set(bits))
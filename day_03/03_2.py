# arr = [3, 6, -2, 7, -1, 1 ,-5, -1, 5, 4]
# N = len(arr)

# for j in range(N):
#     if subset & (1 << j):
#         print(arr[j], end=' ')

# for subset in range(1<<N):
#     print(subset, end='>')
#     for j in range(N):
#         if subset & (1 <<j):
#             print(arr[j], end = '')
#     print()

# for i in range(1, 1 << N):  #i 는 부분집할을 표현
#     Sum = 0
#     for j in range(N):
#         if i & (1<<j):   # arr[j]를 포함하는지
#             Sum += arr[j]

#     if Sum == 0:
#         for j in range(N):
#             if i & (1<<j):   
#                 print(arr[j], end='')
#     print()

#<2진수>
    # 합이 0이되는 부분집합 구하기
arr = [3, 6, -1, 7, -3, 1, -5, -1, 5, 4]
N = len(arr) # 10

for i in range(1, 1 << N): # i는 부분집합을 표현, 공집합은 필요없다는 가정하에 1,
    Sum = 0
    for j in range(N):
        if i & (1 << j): # arr[j]를 포함하는지 / 비트표현에서 j번째 인덱스에 포함하는것인지 아닌지
            Sum += arr[j]
    if Sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=', ')
        print()

#<이진탐색>
def binarySearch(arr, key):

    lo, hi = 0, len(arr) - 1
        # lo=start hi=end

    while lo <= hi:
        mid = (lo + hi) >> 1   # (lo+hi) /2
        if arr[mid] == key:
            break
        if arr[mid] > key:
            hi = mid - 1     # 끝점을 중간 앞으로
        else:
            lo = min + 1     # 시작점을 중간 다음으로
    
    return -1


#재귀호출 while 반복 대신 재귀호출로 구현
def binarySearchs(arr,lo, hi, key):
    if lo > hi: return False
    
    mid = (lo + hi) >> 1  
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binarySearchs(arr, lo, mid - 1, key)     
    else:
        return binarySearchs(arr, mid + 1, hi, key)    
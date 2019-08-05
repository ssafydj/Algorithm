#선택정렬

arr = [64, 25 ,10, 22, 11]
N = len(arr)
# [0, n-1] 에서 최소값의 위치를 찾는다.

minIdx = 0
for j in range(minIdx +1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[0], arr[minIdx] = arr[minIdx], arr[0]

# [1, n-1] 최소값을 찾는다.

minIdx = 1
for j in range(minIdx +1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j

arr[1], arr[minIdx] = arr[minIdx], arr[1]

# [2, n -1]
#.....
# [n-2, n-1] 즉 마지막 2개가 남을 때 까지 반복한다.
print(arr)




print('-------------')

for i in range(N-1):               
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j

arr[i], arr[minIdx] = arr[minIdx], arr[i]



# 셀렉션 알고리즘
# k번째 값 : k 번만 반복하면 알 수 있다.


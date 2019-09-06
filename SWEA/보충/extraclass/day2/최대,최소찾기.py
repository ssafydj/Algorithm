# 1. 최대 최소를 저장할 변수가 필요

arr = [0, 4, 1, 3, 1, 2, 4, 1]

# 최소값 찾기
Min = arr[0]
for i in range(1, len(arr)):
    if Min > arr[i]
        Min = arr[i]
print(Min)

# 최소값 위치 찾기
MinIdx = 0      # 0번 위치를 최소값의 위치로 저장
for i in range(1, len(arr)):
    if arr[MinIdx] > arr[i]:            # 같은 최소값이 있는경우에 
                                        # >= 를 사용하면 뒤에 값이 최소값의 위치로 나옴
        MinIdx = i
print(MinIdx, arr[MinIdx])


# 값을 등장 횟수를 계산
# 자료값을 리스트의 인덱스로 사용한다.
# 자료값이 양의 정수여야 한다.
# 자료값의 범위(최대값)를 알아야 한다.

cnt = [0] * 5   # 값을 넣을 공간 마련
for val in arr:
    cnt[val] = cnt[val] + 1

for i in range(len(cnt)):
    print(i, cnt[i])       # i의 갯수를 보여줌


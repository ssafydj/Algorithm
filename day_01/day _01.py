arr = [55, 7, 78, 12, 42]

n = len(arr)

for j in range(n -1, 0, -1):

​    for i in range(j):

​        if arr[i] > arr[i + 1]:

​            arr[i], arr[i + 1] = arr[i + 1], arr[i?]

print(arr)





#for i in range(n - 1):

 #     if arr[i] > arr[i + 1]:

#             arr[i], arr[i + 1] = arr[i + 1], arr[i?]



# for i in range(n - 2):

#      if arr[i] > arr[i + 1]:

#             arr[i], arr[i + 1] = arr[i + 1], arr[i?]



# for문을 중복하여 위에 처럼 하나로 표현함.



# 최소값 찾기

MIN = arr[0]

for i in range(1, len(arr)):

​    if arr[i] < MIN:

​        MIN = arr[i]



print(MIN)



# 크기별로 정렬 / 총 n-1 번 시행

MIN = 0 # 0번 인덱스에 들어갈 가장 작은 값

for i in range(1, len(arr)):

​    if arr[i] < arr[MIN]:

​        MIN = i

arr[0], arr[MIN] = arr[MIN], arr[0]

print(arr)





for i in range(MIN + 1, len(arr)):

​    if arr[i] < arr[MIN]:

​        MIN = i

arr[1], arr[MIN] = arr[MIN], arr[1]

print(arr)





​    MIN = j



   for i in range(j + 1, len(arr)):

​    if arr[i] < arr[MIN]:

​        MIN = i

arr[1], arr[MIN] = arr[MIN], arr[1]

print(arr)





## 카운팅 정렬 과정

data = [0, 4, 1, 3, 1 ,2, 4, 1]

counts = [0] *5 # 최대값 = 4



for val in data:

​    counts[val] += 1



# 데이터 카운트 완료, 정렬 할 차례



sorted = []

for i in range(len(counts)):

​    for j in range(count[i]):

​        sorted.append(i)

# 카운트 한 횟수를 for 문 돌려서 정렬된 원래 상태로 복구.

print(sorted)





for val in data:

​    count[val] += 1



for i in range(1, len(counts)):

​    counts[i] = counts(i-1) + counts[i]


#<Baby-gin game> (p.19) Ad 유형 중 완전탐색 > 컴퓨터의 최대 장점인 '빠른 계산능력'을 활용

# > 가능한 모든 경우의수를 따져서 답을 구하는 방식.



## 알고리즘 문제 중

# 최적화 문제: 최대 혹은 최소가 되는 경우를 찾는 문제.

# 결정 문제: ex) baby-gin 유형 True False로 나오는 유형 



# 역량테스트 알고리즘 문제는 유형별로 풀이법이 정해져있다. 기본은 '완전 탐색'





for i in range(n):

​    for j in range(n):

​        for k in range(n):

​            print(data[i], data[j], data[k])



# 순열(p.24)

n = len(data)

for i in range(n):

​    for j in range(n):

​        if i == j: continue     # 건너뛰기

​            for k in range(n):

​                if i == k or j == k: continue

​                    print(data[i], data[j], data[k])
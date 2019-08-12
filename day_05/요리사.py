# 이진검색 하기 위해 두 그룹으로 나누는 개념/방식
# > 부분집합, 순열, 조합과 관련된 문제

# 문제를 제대로 읽고 분석해서(문제 조차 이해못하는 경우가 없도록 연습)
# 효율적으로 푸는 방법을 생각하는게 중요
# 코딩은 하다보면 실력은 쌓인다. <> 문제푸는 방법을 찾는게 중요

arr = [10, 20, 30, 40]
N = 4
for set in range(1 << 4):
    A, B = [], []
    for i in range(N):
        if set & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)
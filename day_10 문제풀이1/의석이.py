import sys
sys.stdin = open('의석이.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    arr = [list(input().split()) for _ in range(5)]
    l = [len(i) for i in arr]   # 각 문자열의 길이
    ml = max(l) # 문자열 중 최대길이

    temp = ""
    for i in range(ml):
        for j in range(5):
            if l[j] > i:    # 자신의 문자열의 길이보다 열번호가 작으면 문자 추가하지 않음
                temp += arr[j][i]


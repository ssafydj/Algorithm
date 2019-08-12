#중간을 기준으로 좌/우측의 문자열이 같으면 회문

arr = 'algorithm'
n = len(arr)

# Solution 1
for i in range(n//2):
    # arr[i] <-> arr[n-1-i]  # 교환
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
print(arr)
    # print(''.join(arr))  # list -> string

# Solution 2
if arr[::-1] == arr:
    result = 1
else:
    result = 0



p = 'abcdabcef'
t = 'arjhwaekthastgsadt'

n, m = len(t), len(p)   # n = 텍스트 길이, m = 패턴 길이

# 텍스트에서 패턴이 있을 수 있는 모든 시작위치 1
for i in range(n-m+1):
    for j in range(m):
        if t[i+j] != p[j]:
            break          # break = 위에가 성립하면 else 건너 뜀.
    else:
        print(t[i:i+m])

# 텍스트에서 패턴이 있을 수 있는 모든 시작위치 2
for i in range(n-m+1):
    j = 0
    while j < m  
        if t[i+j] != p[j]:
            break          # break = 위에가 성립하면 else 건너 뜀.
        j += 1
    if j == m:
        print(t[i:i+m])

# t, i ,n  <> p, j, m    

# 고지식한 패턴 검색 알고리즘(p.134)
i = j = 0
while i < n:
    if p[j] == t[i]:
        i, j = i+1, j+1
        if j == m:  # 즉 t와 p가 같으면,
            print(t[i-j:])
            break
    else:
        i = i-+1
        j = 0


# KMP > 불일치가 발생했을 때 i를 그 자리에 멈춰두고 j의 위치를 재설정한다. O(n) 



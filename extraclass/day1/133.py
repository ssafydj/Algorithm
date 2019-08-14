##입력값 받는거 주의
num = list(map(int, input().split()))
result = 0

for i in num:
    result += i
    box = result / len(num)

print(box)
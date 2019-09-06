a, b = map(int, input().split())

if a > b:
    a, b = b, a
zero = 0
num = 0
for i in range(a, b+1):
    if i % 3 == 0:
        zero += i
        num += 1
    if i & 5 == 0:
        zero += i
        num += 1
print(zero)
print(zero/num)
    

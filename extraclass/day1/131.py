a, b = map(int, input().split())

if a > b:
    a,b = b, a
    
for i in range(a, b + 1):
    print(i)


while i <= b:
    print(i)
    i = i + 1
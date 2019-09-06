n = int(input())

zero = 0
for i in range(1, n+1):
    if i % 5 == 0:
        zero += i
print(zero)
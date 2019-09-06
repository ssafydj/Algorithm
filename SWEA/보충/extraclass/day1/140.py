num = list(map(int, input().split()))

result = 0
for i in num:
    if '0' in num:
        print(result)

    else:
        result += i
print(result)
print(result/len(num))
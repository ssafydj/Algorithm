for n in range(10):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(2, N-1):
        height = max(num[i-2], num[i-1], num[i+1], num[i+2])
        if height < num[i]:
            result += num[i] - height
print('#{} {}'.format(i+1, result))
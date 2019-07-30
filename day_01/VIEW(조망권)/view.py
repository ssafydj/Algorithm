for n in range(10):
    N = int(input())
    num = list(map(int, input.split()))

result = 0
for i in range(2, N-1):
        MAX = max(num[i-2], num[i-1], num[i+1], num[i+2])
        if MAX < Num[i]:
                result += num[i] - MAX

print('{} {}'.format(,))

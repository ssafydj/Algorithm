#재귀적 DP (재귀호출 + memoization)

## case 1
memo = [-1] * 100

def fibonacci(n): # n 번째 피보나치 수를 반환
    if n == 1 or n == 0:    #기저 사례를 앞에 두고
        return n
    #이미 답을 구했는지 확인
    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(70))

#################################################
## case 2
memo = [-1] * 100

def fibonacci(n): # n 번째 피보나치 수를 반환
    memo[0], memo[1] = 0, 1         # 이미 답을 알고 있으므로
    for i in range(2, n+1):
        memo[i] = memo[i-1]+memo[i-2]

    return memo[n]
print(fibonacci(70))

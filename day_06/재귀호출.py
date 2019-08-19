def factorial(n):
    # 매개변수 : 문제의 크기를 나타내는 값
    # 반환값: n! (문제의 해)
    if n == 0 or n == 1:
        return 1
        # 재귀호출 하지 않고 종료 > 기저사례
    else:
        return factorial(n-1) * n
        # 재귀 호출
print(factorial(4))

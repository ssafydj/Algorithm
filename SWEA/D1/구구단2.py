a, b= map(int, input().split())

count = 0                                                      # 조건 충족하면 칸 넘김
for i in range(1, 10):
    print('{:2} * {:1} = {:2}'.format(a, i ,a*i), end='    ')  # :2로 칸 조절가능
    count += 1
    if count == 3:                                             # 3개 쌓이면
        print()                                                # 줄 바꾸고
        count = 0                                              # 초기화
print()

count = 0
for i in range(1, 10):
    print('{:2} * {:1} = {:2}'.format(b, i ,b*i), end='    ')
    count += 1
    if count == 3:
        print()
        count = 0
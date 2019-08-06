import sys
sys.stdin = open("2072.txt", "r")

zero = 0
tc = int(input())
for k in range(1, tc + 1):
    n = list(map(int, input().split()))
    # print(n)

    zero = 0      # 1바퀴 돌고 0 초기화하고 다시 들어가는걸 반복!
    for i in n:
        if i % 2 == 1:
            zero = zero + i 
            
   # print(zero)
    
    print('#{} {}'.format(k, zero))


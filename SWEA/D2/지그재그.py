import sys
sys.stdin = open("1986.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n = int(input())
    
    zero = 0
    for num in range(1, n + 1):
        if num % 2:
            zero += num
        else:
            zero += -num

    print("#{} {}".format(k, zero))
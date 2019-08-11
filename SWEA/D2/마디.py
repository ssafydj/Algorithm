import sys
sys.stdin = open("2007.txt", "r")


tc = int(input())
for k in range(1, tc + 1):
    n = input()
    # print(n)

    cnt = 0
    for i in range(2, 27):
        if n[0]+n[1]+n[2] == n[i]+n[i+1]+n[i+2]:
            cnt += 1
    print(cnt)

   


import sys
sys.stdin = open("1989.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n = input()
    # print(n[0])
    for i in range(1, len(n) + 1):
        if len(n) % 2 == 0:     #n이 짝수 자리수
            if n[::] == n[::-1]:
                print(1)
            else:
                print(0)
        else: 
            n[0]+n[1] == n[i-1]+n[i-2]
            print(1)
            else:
                print(0)
            

            
            

            

    

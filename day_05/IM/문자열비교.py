import sys
sys.stdin = open("4864.txt", "r")

tc = int(input())

for k in range(1, tc + 1):
    str1 = list(map(str, input().split()))
    str2 = list(map(str, input().split()))
    # print(str1)
    # print(str2)

    n = (''.join(str2))
    m = (''.join(str1))
    # print(n)
    # print(m)
    for i in range(tc):
        if m[::] in n[::]:
            result = '1'
        else:
            result + '0'
    print(result)










    # for i in range(n-m+1):
    #     for j in range(m):
    #         if str2[i+j] != str1[j]:
    #             break
    #     else:
    #         print(str2[i:i+m]) 

    

    

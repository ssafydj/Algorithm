import sys
sys.stdin = open("1945.txt", "r")

tc = int(input())
# print(tc)
for _ in range(1, tc+1):
    n = int(input())
    # print(n)

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for k in range(1, n + 1):
       if n % 2 == 0:
        a += 1
            if n % 3 == 0:
                b += 1
            if n % 5 == 0:
                c += 1
                if n % 7 == 0:
                    d += 1
                    if n % 11 == 0:
                        e += 1
    
    print('#{} {} {} {} {} {}'.format(k, a, b, c, d, e))
        
       


#         b = 0
#         if n & 3 == 0:
#             b += 1

#         c = 0
#         if n % 5 == 0:
#             c += 1
    
#         d = 0
#         if n % 7 == 0:
#             d += 1
    
#         e = 0
#         if e %11 == 0:
#             e += 1

# print('#{} {} {} {} {} {}'.format(k, a, b, c, d, e))
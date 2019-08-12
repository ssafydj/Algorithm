import sys
sys.stdin = open("1284.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    p, q, r, s, w= list(map(int, input().split()))
    # print(p, q, r, s, w)

    if w <= r:
        result = q
        if p*w < q:
            result = p*w
    else:
        if q + (w-r)*s > p*w:
            result = p*w
        else:
            result = q + (w-r)*s 

    print("#{} {}".format(k, result))
     

    
    # if p*w > q:
    #     result = q
    #     if w >r: 
    #         result = q + (w-r)*s
    # else:
    #     result = p*w
    # print("#{} {}".format(k, result))
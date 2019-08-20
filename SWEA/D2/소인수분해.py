import sys
sys.stdin = open("1945.txt", "r")

tc = int(input())
# print(tc)

primea = 0
nums = [2, 3, 5, 7, 11]
for r in range(1, tc+1):
    r = int(input())
    # print(r)

    for num in nums:
        while r % num == 0:
            primea += 1
            r = r / num

        if primea == []:
            primea += 0

    print(primea)






    # print('#{} {} {} {} {} {}'.format(r, a, b, c, d, e))
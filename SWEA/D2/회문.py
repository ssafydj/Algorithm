import sys
sys.stdin = open("1989.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    arr = input()
    m = len(arr)

    for i in range(m//2):
        if arr[i] == arr[m-1-i]:
            result = '1'
        else:
            result = '0'
    # print(result)


    print('#{} {}'.format(k, result))
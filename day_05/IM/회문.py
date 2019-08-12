import sys
sys.stdin = open("4861.txt", "r")

tc = int(input())
n, m = map(int, input().split())
for k in range(1, n + 1):
    arr = input()
    l = len(arr)
    # print(arr)
    
    for i in range(l//2):
        if arr[i] == arr[l-1-i]:
            result = arr
    print(result)












# tc = int(input())
# n , m = map(int, input().split())
# for k in range(1, n + 1):
#     for a in range(1, m + 1):
#     arr = input()
#     m = len(arr)
#     # print(arr)

#     for i in range(m//2):
#         if arr[i] == arr[m-1-i]:
#             result = arr
#     print(result)
    



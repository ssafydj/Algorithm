import sys
sys.stdin = open("중간값찾기.txt", "r")

N = int(input())
num = list(map(int, input().split()))
# print(num)


arranged = sorted(num)
print(arranged[N // 2])


import sys
sys.stdin = open('삼성버스.txt', 'r')

t = int(input())
tc = int(input())

for i in range(1, tc+1):
    ai, bi = map(int, input().split())
    arr = [0] * 6

    for j in range(ai, bi+1):
        arr[j] += 1

    print(arr)




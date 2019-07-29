import sys
sys.stdin = open('input.txt', 'r')

arr = []
N = int(input())
arr = list(map(int, input().split()))
print(N)
print(arr)

height = len(arr)
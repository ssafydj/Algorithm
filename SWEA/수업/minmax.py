import sys
sys.stdin = open('4828.txt', 'r')

tc = int(input())
# print(tc)
for i in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(n)
    # print(nums)
    Max = nums[0]
    Min = nums[0]
    for j in range(1, len(nums)):
        if nums[j] > Max:
            Max = nums[j]
        if nums[j] < Min:
            Min = nums[j]
        result = Max - Min
    # print(result)

    print('#{} {}'.format(i+1, result))
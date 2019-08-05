TCS = int(input())
for TC in range(TCS):
    cards = int(input()) # 길이
    nums = input         # 카드 정보, 문자열

    ztot = [0] * 10
    
for i in range(cards):
    if nums[i]:
        ztot[int(nums[i])] += 1

maxi = ztot[0]
for i in range(1, len(ztot)):
    if maxi <= ztot[i]:
        maxi = ztot[i]
        idx = i

print('#%d %d %d' % (TC+1, idx, maxi))

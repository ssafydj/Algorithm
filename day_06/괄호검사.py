import sys
sys.stdin = open('4866.txt', 'r')
tc = int(input())
# print(tc)

for k in range(1, tc+1):
    paren = input().split()
    # print(paren)

    result = []
    for ch in paren:
        if ch == '(':
            result.append(ch)
        else:
            if len(result) == 0:
                break
            if ')' and result.pop !='(':
                return 0
    print(result)











    # S = []  # 저장소
    #
    #
    # def push(item):
    #     S.append(item)
    #
    #
    # def pop():  # 항상 empty 상태 체크
    #     return S.pop()
    #
    #
    # def isEmpty():
    #     return len(S) == 0
    #
    # for ch1 in paren:
    #     if ch1 == '(':
    #         push(ch1)
    #
    #     else:
    #         if isEmpty():
    #             # 잘못된 표현
    #             break
    #         if ')' and pop() != '(':
    #             # 잘못된 표현
    #             break
    #
    # for ch2 in paren:
    #     if ch2 == '{':
    #         push(ch2)
    #     else:
    #         if isEmpty():
    #             # 잘못된 표현
    #             break
    #         if '}' and pop() != '{':
    #             # 잘못된 표현
    #             break
    # print(ch1)
    # print(ch2)

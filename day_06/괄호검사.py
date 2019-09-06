import sys
sys.stdin = open('4866.txt', 'r')
tc = int(input())
# print(tc)

for k in range(1, tc+1):
    paren = input().split()
    # print(paren)

    stack = []
    ans = True
    for ch in paren:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch ==')' or ch =='}':
            if len(stack) == 0:
                ans = False
                break

                tmp = stack.pop()

                if ch == ')' and tmp != '(':
                    ans = False
                    break
                if ch == '}' and tmp != '{':
                    ans = False
                    break
    if ans and len(stack) != 0:
        ans = False

    print(ans)




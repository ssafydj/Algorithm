def check_paren(item):
    stack = []

    for ch in item:
        if ch == '(':   # 여는 괄호일 때
            stack.append(ch)
        else:
            if len(stack) != 0: # 닫는 괄호
                stack.pop()
            else:               # len = 0 즉, 원소가 없는 경우
                return False
    if len(stack) > 0:          # 괄호가 짝이 맞지 않는 경우
        return False

    return True     # 여는/닫는 괄호 짝이 잘 맞는 경우

str1 = '()()((()))'
str2 = '((()((((()()((()())((()))))'

if check_paren(str1):
    print('OK')
else:
    print('FAIL')

if check_paren(str2):
    print('OK')
else:
    print('FAIL')

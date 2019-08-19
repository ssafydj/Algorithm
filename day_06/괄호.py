S = []          # 저장소
def push(item):
    S.append(item)

def pop(): # 항상 empty 상태 체크
    return S.pop()

def isEmpty():
    return len(S) == 0

paren = '()()((()))'

for ch in paren:
    if ch == '(':
        push(ch)
    else:
        if isEmpty():
            #잘못된 표현
            break
        if ')'and pop() !='(':
            # 잘못된 표현
            break

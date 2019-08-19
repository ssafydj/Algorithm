# C - style

S = [0] * 3 # 저장소
top = -1     # 마지막에 저장된 자료의 인덱스

def push(item):
    global top
    # full 상태를 체크
    if top == 2: return
    top += 1
    S[top] = item


def pop():
    global top
    # empty 상태 체크
    if top == -1: return
    ret = S[top]
    top -= 1
    return ret


for i in range(3):        # 저장소의 크기가 3이므로 3회 이하만 반복가능
    push(i)

print(pop())
print(pop())
print(pop())

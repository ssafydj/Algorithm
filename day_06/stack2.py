# python-style

S = []          # 저장소
def push(item):
    S.append(item)

def pop(): # 항상 empty 상태 체크
    return S.pop()

def isEmpty():
    return len(S) == 0

for i in range(3):
    push(i)

while not isEmpty():
    print(pop())


print(pop())
print(pop())
print(pop())


# # deque 사용
# from collections import deque
# import time             #실행시간 확인 모듈
# start = time.time()
# S= deque()
# N = 1000000
# for i in range(N):
#     S.append(i)
# while S:        #empty 상태 체크 만약 S가 비어있다면 false로 while 문 종료됨
#     S.pop()
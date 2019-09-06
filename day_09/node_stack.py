class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def push(i): # 원소 i를 스택 top(맨 앞)에 push
    global top
    top = Node(i, top) # 새로운 노드 생성


def pop(): # 스택의 pop에 pop
    global top
    if top == None: # 빈 리스트 이면
        print('error')
    else:
        data = top.data
        top = top.link # top 이 가리키는 노드를 바꿈
        return data

top = None
push(3)  # 노드 생성하여 아래부터 3->4->5->6 순으로 stack 쌓임
push(4)
push(5)
push(6)
pop()

while top.link != None:
    print(top.data, end='->')
    top = top.link
print(top.data)

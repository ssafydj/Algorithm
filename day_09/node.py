class Node:
    def __init__(self, data, link): 
        self.data = data
        self.link = link


def addtoFirst(data):   # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head) # 새로운 노드 생성


def add(pre, data): # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data): # 마지막에 데이터 삽입
    global Head
    if Head == None: # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None: # 마지막 노드 찾을때까지
            p = p.link
        p.link = Node(data, None)


data = [1, 2, 3, 4]
Head = None

# for i in range(len(data)):
#     addtoFirst(data[i])

for i in range(len(data)):
    addtoLast(data[i])

# add(Head, 8)


while Head.link != None:
    print(Head.data, end ='>')
    Head = Head.link
print(Head.data)
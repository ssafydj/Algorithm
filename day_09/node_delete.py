def delete(pre): # pre 다음 노드 삭제
    if pre == None or pre,link == None:
        print('error')
    else:
        pre.link = pre.link.link


def deleteFirst(): # 처음 노드 삭제
    global Head
    if pre == None:
        print('error')
    else:
        Head = Head.link
        
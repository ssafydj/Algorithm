# 각 정점의 인접정점을 가져오기

import sys
sys.stdin = open('DFS_input.txt', 'r')

V, E = map(int, input().split())  # 정점수, 간선수

G = [[] for _ in range(V+1)]      # 정점 번호: 1~V

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

    for i in range(1, V+1):
        print(i, '-->', G[i])

##########################################

# v에 방문하지 않는 인접정점 w찾기

def DES(v):             # v: 시작점
    S = []
    visit = [False] * (V+1)
    visit[v] = True # 시작점을 방문한다.
    S.append(v)     # 시작점을 스택에 push

    while S: #빈 스택이 아닐 동안 동작
        # v의 방문하지 않은 인접 정점을 찾는다. --> w
        for w in G[v]:
            if not visit[w]:
                visit[w] = True  # w를 방문하고
                S.append(v)     # v를 스택에 push
                v = w           # w를 현재 방문하는 정점으로 설정
                break
        else:
            v = S.pop()





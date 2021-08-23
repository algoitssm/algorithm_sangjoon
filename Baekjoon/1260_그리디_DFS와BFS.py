from collections import deque


def bfs(n: int):
    dq = deque([n])

    while dq:
        e = dq.popleft()

        if not visited[e]:
            visited[e] = 1
            bfs_lst.append(e)

            for node in lst[e]:
                if not visited[node]:
                    dq.append(node)


def dfs(n: int):
    visited[n] = 1
    dfs_lst.append(n)

    for node in lst[n]:
        if not visited[node]:
            dfs(node)


n, m, v = map(int, input().split())

lst = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    lst[l].append(r)
    lst[r].append(l)

for l in lst:
    l.sort()

visited = [0] * (n + 1)  # 방문표시 초기화
dfs_lst = []
dfs(v)

visited = [0] * (n + 1)  # 방문표시 초기화
bfs_lst = []
bfs(v)

print(*dfs_lst)
print(*bfs_lst)
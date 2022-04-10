from collections import deque


def bfs(n: int):
    dq = deque([n])

    while dq:
        e = dq.popleft()
        for node in graph[e]:
            if not parent[node]:
                parent[node] = e
                dq.append(node)


n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for i in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

parent = [0] * (n + 1)

bfs(1)


print("\n".join(map(str, parent[2:])))

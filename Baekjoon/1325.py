from collections import deque


def bfs(n: int):
    visited = [0] * (n + 1)
    cnt = 0

    dq = deque([n])
    visited[n] = 1  # 감염 초기화

    while dq:
        e = dq.popleft()
        if e in graph:  # 추가 감염가능 확인
            for comp in graph[e]:
                if not visited[comp]:  # 감염되지 않은 경우
                    visited[comp] = 1
                    dq.append(comp)
                    cnt += 1
    return cnt


n, m = map(int, input().split())

graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
max_cnt = 0
max_key = []

for key, _ in graph.items():
    cnt = bfs(key)
    if cnt > max_cnt:
        max_cnt, max_key = cnt, [key]
    elif cnt == max_cnt:
        max_key.append(key)

max_key.sort()
print(*max_key)

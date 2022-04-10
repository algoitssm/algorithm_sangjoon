from collections import defaultdict

n, m = map(int, input().split())
INF = int(1e10)
gh = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, d = map(int, input().split())
    gh[a - 1][b - 1] = min(gh[a - 1][b - 1], d)

dist = [INF] * n
dist[0] = 0

for _ in range(n - 1):
    for i in range(n):
        for j in range(n):
            dist[j] = min(dist[j], dist[i] + gh[i][j])

for i in range(n):
    for j in range(n):
        if dist[j] > dist[i] + gh[i][j]:
            dist[j] = -1

for i in range(1, n):
    if dist[i] == -1 or dist[i] == INF:
        print(-1)
        break
    print(dist[i])

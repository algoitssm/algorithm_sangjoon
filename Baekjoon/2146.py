from collections import defaultdict, deque
from itertools import permutations


def bfs(r, c):
    dq = deque([(r, c)])
    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if mp[nr][nc] and not v[nr][nc]:
                    v[nr][nc] = cnt
                    d[cnt].append((nr, nc))
                    dq.append((nr, nc))


n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
res = [2 * n]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

v = [[0] * n for _ in range(n)]
d = defaultdict(list)
cnt = 0
for i in range(n):
    for j in range(n):
        if mp[i][j] and not v[i][j]:
            cnt += 1
            v[i][j] = cnt
            d[cnt].append((i, j))
            bfs(i, j)

for i, j in permutations(d, 2):
    for r1, c1 in d[i]:
        for r2, c2 in d[j]:
            l = abs(r1 - r2) + abs(c1 - c2) - 1
            res[0] = min(res[0], l)

print(res[0])

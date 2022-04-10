def dfs(n):
    for i in mp[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)


n, m = map(int, input().split())
mp = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    u, v = map(int, input().split())
    mp[u - 1].append(v - 1)
    mp[v - 1].append(u - 1)

res = 0
for s in range(n):
    if not visited[s]:
        visited[s] = 1
        res += 1
        dfs(s)
print(res)

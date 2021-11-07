n = int(input())
m = int(input())
INF = int(1e10)

mp = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, d = map(int, input().split())
    mp[a-1][b-1] = min(mp[a-1][b-1], d)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                mp[i][j] = 0
            mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

for i in range(n):
    for j in range(n):
        if mp[i][j] == INF:
            mp[i][j] = 0
    print(*mp[i], sep=" ")

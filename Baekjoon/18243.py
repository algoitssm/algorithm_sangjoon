# 플로이드 와샬
def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j and mp[i][j]:
                    continue
                mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

    for i in range(n):
        for j in range(i+1, n):
            if mp[i][j] > 6:
                return "Big World!"

    return "Small World!"


n, k = map(int, input().split())
mp = [[float("inf")]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    mp[a-1][b-1] = 1
    mp[b-1][a-1] = 1

print(floyd_warshall())

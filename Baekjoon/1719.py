n, m = map(int, input().split())

mp = [[float("inf")] * n for _ in range(n)]  # 최단경로
res = [["-"] * n for _ in range(n)]  # 방문 경로

for _ in range(m):  # 초기화
    a, b, d = map(int, input().split())
    mp[a - 1][b - 1], mp[b - 1][a - 1] = d, d
    res[a - 1][b - 1], res[b - 1][a - 1] = b, a

# 플로이드-와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if mp[i][k] + mp[k][j] < mp[i][j]:  # 최단경로일 경우
                mp[i][j] = mp[i][k] + mp[k][j]
                res[i][j] = res[i][k]


for r in res:
    print(*r)

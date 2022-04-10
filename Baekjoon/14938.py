n, m, r = map(int, input().split())
items = list(map(int, input().split()))
mp = [[float("inf")] * n for _ in range(n)]


for _ in range(r):
    a, b, l = map(int, input().split())
    mp[a - 1][b - 1] = l
    mp[b - 1][a - 1] = l

# 플로이드 와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                mp[i][j] = 0
            mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

# 거리값 내의 아이템 수 최대값 반환
res = 0
for i in range(n):
    res = max(res, sum([items[j] for j in range(n) if mp[i][j] <= m]))

print(res)

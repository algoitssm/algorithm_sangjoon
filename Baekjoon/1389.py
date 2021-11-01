# 플로이드 와샬
n, m = map(int, input().split())
mp = [[n]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    mp[a-1][b-1] = 1
    mp[b-1][a-1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or mp[i][j] == 1:
                continue
            if mp[i][k] and mp[k][j]:
                mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

res = [0, n**2]
for i in range(n):
    t = sum(mp[i])
    if t < res[1]:
        res = [i+1, t]

print(res[0])

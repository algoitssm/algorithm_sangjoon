# 플로이드 와샬 알고리즘

n = int(input())
mp = [[0] * n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            mp[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if mp[i][k] and mp[k][j]:
                mp[i][j] = 1

for l in mp:
    print(*l)

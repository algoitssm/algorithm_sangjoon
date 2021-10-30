# 플로이드 와샬

n = int(input())
mp = [list(input()) for _ in range(n)]
gh = [[0]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if mp[i][j] == "Y":
                gh[i][j] = 1

            if mp[i][k] == "Y" and mp[k][j] == "Y":
                gh[i][j] = 1

res = 0
for i in range(n):
    res = max(res, sum(gh[i]))

print(res)

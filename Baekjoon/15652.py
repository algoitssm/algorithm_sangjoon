def dfs(s, m, lst):
    if m == 0:
        print(" ".join(map(str, lst)))
        return
    for i in range(s, n + 1):
        dfs(i, m - 1, lst + [i])


n, m = map(int, input().split())
dfs(1, m, [])

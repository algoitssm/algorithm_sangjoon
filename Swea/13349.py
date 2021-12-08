ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m, l = map(int, input().split())
    nodes = []
    for i in range(n):
        lst = list(map(int, input().split()))
        for j in range(m):
            if lst[j] == 1:
                nodes.append((i, j))
            if lst[j] == 2:
                s = (i, j)
            if lst[j] == 3:
                e = (i, j)
    nodes = [s, e] + nodes

    t = len(nodes)
    inf = float("inf")
    mp = [[inf] * t for _ in range(t)]
    for i in range(t):
        for j in range(t):
            if abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1]) <= l:
                mp[i][j] = 1

    # 플루이드 와샬
    for k in range(t):
        for i in range(t):
            for j in range(t):
                if i == j and mp[i][j]:
                    continue
                mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])

    ans.append("#{} {}".format(
        test, mp[0][1]-1 if mp[0][1]-1 != inf else -1))

print(*ans, sep="\n")

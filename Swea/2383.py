def check_time(stair: tuple, people: list):
    sr, sc = stair
    time = mp[sr][sc]
    l = [abs(pr-sr) + abs(pc-sc) + time + 1 for pr, pc in people]
    l.sort()

    for i in range(3, len(l)):
        l[i] += l[i-3] - (l[i]-time) if l[i-3] - (l[i]-time) > 0 else 0

    return l[-1] if l else 0


ans = []
test_case = int(input())
for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    p, s = [], []
    cnt = float("inf")

    for i in range(n):
        for j in range(n):
            if mp[i][j] == 1:
                p.append((i, j))
            elif mp[i][j] != 0:
                s.append((i, j))

    for i in range(1 << len(p)):
        p1, p2 = [], []
        for j in range(len(p)):
            if i & (1 << j):
                p1.append(p[j])
            else:
                p2.append(p[j])

        t1 = check_time(s[0], p1)
        t2 = check_time(s[1], p2)
        cnt = min(cnt, max(t1, t2))
    ans.append("#{} {}".format(test, cnt))

print(*ans, sep="\n")

n, m = map(int, input().split())

store = int(input())
gp = {i: [] for i in range(1, 5)}

for _ in range(store):
    d, p = map(int, input().split())
    if d == 1:
        gp[1].append((p))
    if d == 2:
        gp[2].append((p))
    if d == 3:
        gp[3].append((0))
    if d == 4:
        gp[4].append((n))

x, y = map(int, input().split())
ans = 0

for d, lst in gp:
    if x == d:
        for temp in lst:
            ans += abs(y - temp)
    if x == 1:
        pass
    if x == 2:
        pass
    if x == 3:
        pass
    if x == 4:
        pass

# 문제 푼 시간
from itertools import combinations
from collections import defaultdict, OrderedDict


def check_collision(a, b):
    xa, ya, da, ka = a
    xb, yb, db, kb = b

    if (xa-xb) == 0 or (ya-yb) == 0:
        if ya > yb:
            if da != 1 or db != 0:
                return 0, 0

        if ya < yb:
            if da != 0 or db != 1:
                return 0, 0

        if xa > xb:
            if da != 2 or db != 3:
                return 0, 0

        if xa < xb:
            if da != 3 or db != 2:
                return 0, 0

    if abs(xa-xb) - abs(ya-yb):
        return 0, 0

    if (xa > xb and ya > yb):
        if (da, db) not in [(1, 3), (2, 0)]:
            return 0, 0

    if (xa > xb and ya < yb):
        if (da, db) not in [(0, 3), (2, 1)]:
            return 0, 0

    if (xa < xb and ya > yb):
        if (da, db) not in [(3, 0), (1, 2)]:
            return 0, 0

    if (xa < xb and ya < yb):
        if (da, db) not in [(3, 1), (0, 2)]:
            return 0, 0

    return 1, round((abs(xa-xb) + abs(ya-yb))/2, 1)


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    elements = [tuple(map(int, input().split())) for _ in range(n)]
    collisions = defaultdict(list)
    visited = set()
    res = 0
    for a, b in combinations(elements, 2):
        chk, t = check_collision(a, b)
        if chk:
            print(a, b)
            collisions[t].append((a, b))
    collisions = list(sorted(collisions.items()))
    # print(collisions)

    for t, eles in collisions:
        tv = set()
        for ele in eles:
            a, b = ele
            if a not in visited and b not in visited:
                tv.add(a)
                tv.add(b)
        if tv:
            print(t, tv)
        for e in tv:
            visited.add(e)
            res += e[3]
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")

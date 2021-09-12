from itertools import combinations
import sys


input = sys.stdin.readline

n = int(input())
tr = {i: [0, 0] for i in range(1, n + 1)}

for _ in range(n - 1):
    p, node, length = map(int, input().split())
    tr[p][0] = -1
    tr[node].extend(tr[p][2:] + [p])
    tr[node][1] = tr[p][1] + length

leaf_l = [(tr[idx][1], idx) for idx, v in tr.items() if v[0] == 0]
ans = 0
a, idx_a = max(leaf_l, key=lambda x: x[0])

for b, idx_b in leaf_l:
    parents = set(tr[idx_a][2:]).intersection(set(tr[idx_b][2:]))
    temp = a + b - 2 * (max([tr[i][1] for i in parents]))
    if temp > ans:
        ans = temp

print(ans)
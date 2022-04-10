import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def make_tree(n: int, p: int):
    for node in lst[n]:
        if node != p:
            tr[n].append(node)
            make_tree(node, n)


def count_subnode(n: int):
    size[n] = 1
    for node in tr[n]:
        if not size[node]:
            count_subnode(node)
            size[n] += size[node]


n, r, q = map(int, input().split())
lst = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

tr = [[] for _ in range(n + 1)]
make_tree(r, -1)

size = [0] * (n + 1)
for _ in range(q):
    ur = int(input())
    count_subnode(ur)
    print(size[ur])

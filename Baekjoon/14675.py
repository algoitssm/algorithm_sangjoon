from sys import stdin

input = stdin.readline

n = int(input())
tr = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tr[a].append(b)
    tr[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1 and len(tr[k]) == 1:
        print("no")
    else:
        print("yes")

from collections import defaultdict, deque


def convert(n: str):
    return str(int(n) % 1000000007)


def bfs(a, b):
    dq = deque([(a, lst[a], [])])

    while dq:
        s, res, v = dq.popleft()
        for e in dct[s]:
            if e not in v:
                if e == b:
                    return convert(res + lst[e])
                dq.append((e, convert(res + lst[e]), v + [e]))


n, q = map(int, input().split())
lst = [0] + list(input().split())

dct = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    dct[a].append(b)
    dct[b].append(a)


for _ in range(q):
    a, b = map(int, input().split())
    if a == b:
        print(lst[a])
        continue
    print(bfs(a, b))

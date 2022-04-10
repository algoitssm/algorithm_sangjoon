import heapq


def djikstra():
    heap = []
    heapq.heappush(heap, (0, 0))
    while heap:
        l, s = heapq.heappop(heap)

        if s == d:
            return

        for e, tl in tr[s]:
            if l + tl <= res[e]:
                res[e] = l + tl
                heapq.heappush(heap, (l + tl, e))


n, d = map(int, input().split())
res = [d] * (d + 1)
tr = {i: [(i + 1, 1)] for i in range(d)}

for _ in range(n):
    s, e, l = map(int, input().split())
    if s <= d and e <= d:
        tr[s].append((e, l))

djikstra()
print(res[d])

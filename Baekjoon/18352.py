import heapq
from collections import defaultdict


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0

    while heap:
        d, s = heapq.heappop(heap)
        for e in graph[s]:
            if d >= distance[e]:
                continue

            if d + 1 == k:
                chk[0] = True

            distance[e] = d + 1
            heapq.heappush(heap, (d + 1, e))


n, m, k, x = map(int, input().split())
graph = defaultdict(list)
distance = [float("inf")] * (n + 1)
chk = [False]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dijkstra(x)

if not chk[0]:
    print(-1)
else:
    for idx, d in enumerate(distance):
        if d == k:
            print(idx)

# 플루이드 와샬
n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j])


for _ in range(m):
    a, b, c = map(int, input().split())
    if mp[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")


## 다익스트라: 틀렸음
# from copy import deepcopy
# import heapq


# def dijkstra(s):
#     heap = []
#     heapq.heappush(heap, (0, s))

#     while heap:
#         d, s = heapq.heappop(heap)
#         for idx, e in enumerate(mp[s]):
#             if idx in (0, s):
#                 continue
#             if d + e >= distance[s]:
#                 continue
#             distance[s] = d + e
#             heapq.heappush(heap, (d+e, idx))


# n, m = map(int, input().split())
# mp = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     distance = deepcopy(mp[a])
#     dijkstra(a)
#     if distance[b] <= c:
#         print("Enjoy other party")
#     else:
#         print("Stay here")

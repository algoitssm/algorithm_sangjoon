from collections import defaultdict
import heapq
import math


# 노드간 거리 계산
def get_length(a, b):
    return ((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2) ** (1/2)


# 다익스트라 알고리즘
def djiktra():
    heap = []
    heapq.heappush(heap, (0, 0))
    dist[0] = 0
    while heap:
        l, node = heapq.heappop(heap)

        if node == n-1:
            return l

        for k, v in mp[node].items():
            if l+v < dist[k]:
                dist[k] = l + v
                heapq.heappush(heap, (l+v, k))


n, w = map(int, input().split())
m = float(input())

tr = [[] for _ in range(n)]
lst = []
dist = [float("inf")]*n

for _ in range(n):
    r, c = map(int, input().split())
    lst.append((r, c))

for _ in range(w):
    a, b = map(int, input().split())
    tr[a-1].append(b-1)
    tr[b-1].append(a-1)

# 연결가능 트리 생성
mp = defaultdict(dict)
for i in range(n):
    for j in range(i+1, n):
        if j in tr[i]:  # 보존된 발전소
            mp[i][j], mp[j][i] = 0, 0
            continue

        l = get_length(lst[i], lst[j])
        if l <= m:  # 이동가능 발전소
            mp[i][j], mp[j][i] = l, l


res = djiktra()
print(math.floor((res*1000)))

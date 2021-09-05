from sys import stdin
from collections import deque


n, w = map(int, input().split())
lst = [list(map(int, stdin.readline().split())) for _ in range(n - 1)]

cnt = 0
visited = [0] * (n + 1)

# 최하단 노드 탐색
for a, b in lst:
    if visited[a]:
        if visited[a] == 1:
            n -= 1

    if visited[b]:
        if visited[b] == 1:
            n -= 1

    visited[a] += 1
    visited[b] += 1

# 최상단 노드인 1이 한 개의 자식 노드를 가질 경우
if visited[1] == 1:
    n -= 1


print(w / n)

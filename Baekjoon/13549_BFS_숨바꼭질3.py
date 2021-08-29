## 힙큐 사용
# import heapq

# def bfs(n):
#     queue = []
#     max_num = 100001
#     visited = [-1] * max_num
#     visited[n] = 0
#     dx = [-1, 1]
#     heapq.heappush(queue, [visited[n], n])

#     while queue:
#         cnt, x = heapq.heappop(queue)
#         if x == k:
#             return cnt
#         nx = x * 2
#         if nx < max_num and visited[nx] == -1:
#             if visited[nx] == -1:
#                 if nx == k:
#                     return cnt
#                 visited[nx] = cnt
#                 heapq.heappush(queue, [cnt, nx])

#         for i in range(2):
#             nx = x + dx[i]
#             if 0 <= nx < max_num and visited[nx] == -1:
#                 if nx == k:
#                     return cnt + 1
#                 visited[nx] = cnt + 1
#                 heapq.heappush(queue, [cnt + 1, nx])


# n, k = map(int, input().split())
# print(bfs(n))


## 디큐 사용
from collections import deque


def bfs(n):
    dq = deque([n])
    visited[n] = 0

    while dq:
        dx = [-1, 1]
        x = dq.popleft()
        nx = x * 2
        if nx < max_num and visited[nx] == -1:
            visited[nx] = visited[x]
            dq.appendleft(nx)
            if nx == k:
                return visited[x]

        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < max_num and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                dq.append(nx)
                if nx == k:
                    return visited[x] + 1


n, k = map(int, input().split())

max_num = 100001
visited = [-1] * max_num

bfs(n)
print(visited[k])
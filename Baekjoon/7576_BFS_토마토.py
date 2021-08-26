from collections import deque


def bfs(start: list):
    global total
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    dq = deque(start)

    while dq:
        x, y, cnt = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not grf[nx][ny]:
                    grf[nx][ny] = 1
                    total -= 1
                    if not total:
                        return cnt
                    dq.append((nx, ny, cnt + 1))
    return -1


m, n = map(int, input().split())
grf = [list(map(int, input().split())) for _ in range(n)]

start = []
total = m * n
for i in range(n):
    for j in range(m):
        if grf[i][j] == -1:
            total -= 1
        if grf[i][j] == 1:
            start.append((i, j, 1))
            total -= 1


if total:
    print(bfs(start))
else:  # 모두 익은 경우
    print(0)
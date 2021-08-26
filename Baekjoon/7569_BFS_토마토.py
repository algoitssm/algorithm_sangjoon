from collections import deque


def bfs(start: list):
    global total
    dx = [0, 0, 1, 0, -1, 0]
    dy = [0, 0, 0, 1, 0, -1]
    dz = [1, -1, 0, 0, 0, 0]

    dq = deque(start)
    while dq:
        z, x, y, cnt = dq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if not grf[nz][nx][ny]:
                    grf[nz][nx][ny] = 1
                    total -= 1
                    if not total:
                        return cnt
                    dq.append((nz, nx, ny, cnt + 1))
    return -1


m, n, h = map(int, input().split())
grf = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
start = []
total = m * n * h

for k in range(h):
    for i in range(n):
        for j in range(m):
            if grf[k][i][j] == -1:
                total -= 1
            if grf[k][i][j] == 1:
                start.append((k, i, j, 1))
                total -= 1

if total:
    print(bfs(start))
else:  # 모두 익은 경우
    print(0)
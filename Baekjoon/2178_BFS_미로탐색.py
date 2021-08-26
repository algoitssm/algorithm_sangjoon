from collections import deque


def bfs(x: int, y: int):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dq = deque([[x, y, 1]])
    mp[x][y] = 0

    while dq:
        x, y, cnt = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mp[nx][ny] == "1":
                    mp[nx][ny] = 0
                    if nx == n - 1 and ny == m - 1:
                        return cnt + 1
                    dq.append([nx, ny, cnt + 1])


n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]

ans = bfs(0, 0)
print(ans)
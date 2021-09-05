from collections import deque
from pprint import pprint


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    dq = deque([(x, y, 0)])
    mp[x][y] = 1

    while dq:
        x, y, cnt = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if nx == n - 1 and ny == m - 1:  # 공주 발견 시 종료
                    ans.append(cnt + 1)
                    return

                if mp[nx][ny] == 0 and cnt < t - 1:  # 이동 가능시 방문표시 후 이동
                    mp[nx][ny] = 1
                    dq.append((nx, ny, cnt + 1))

                if mp[nx][ny] == 2 and cnt < t - 1:  # 검 발견시 최소 경로로 탐색
                    mp[nx][ny] = 1
                    cnt += (n - 1 - nx) + (m - 1 - ny) + 1
                    if cnt <= t:
                        ans.append(cnt)

    return


n, m, t = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

ans = []
bfs(0, 0)

if ans:
    print(min(ans))
else:
    print("Fail")

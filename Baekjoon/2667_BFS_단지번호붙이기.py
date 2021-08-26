from collections import deque


def bfs(x: int, y: int):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    dq = deque([[x, y]])  # 초기화
    grf[x][y], cnt = 0, 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if grf[nx][ny]:  # 방문 하지 않았을 경우
                    grf[nx][ny] = 0
                    cnt += 1
                    dq.append([nx, ny])
    return cnt


n = int(input())
grf = [list(map(int, input())) for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if grf[i][j]:  # 방문하지 않았을 경우
            ans.append(bfs(i, j))

ans.sort()

print(len(ans))
for num in ans:
    print(num)
from collections import deque


def bfs(x, y):
    global check
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 디큐 초기화
    dq = deque([[x, y]])
    visited[x][y] = True

    # 연합 초기화
    union = [(x, y)]
    total_sum = nations[x][y]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                    dq.append([nx, ny])
                    visited[nx][ny] = 1
                    total_sum += nations[nx][ny]
                    union.append((nx, ny))
                    check = True  # 연합생성 확인

    for x, y in union:  # 연합 인구 수정
        nations[x][y] = total_sum // len(union)


n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    visited = [[0] * n for _ in range(n)]
    check = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    if not check:  # 연합이 생기지 않을 때까지 반복
        break

    cnt += 1


print(cnt)

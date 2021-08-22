from collections import deque
from itertools import combinations
from copy import deepcopy


def bfs(start: list):
    dq = deque(start)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 3
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_laboratory[nx][ny] == 0:
                new_laboratory[nx][ny] = 2
                dq.append([nx, ny])
                cnt += 1
    return cnt


n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]

virus = []
clean = []
ans = 0
for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 2:  # 감염 초기화
            virus.append([i, j])
        if laboratory[i][j] == 0:  # 미감염 초기화
            clean.append([i, j])

walls = list(combinations(clean, 3))

for wall in walls:
    new_laboratory = deepcopy(laboratory)  # 벽 생성 지도 복사
    for x, y in wall:
        new_laboratory[x][y] = 1  # 벽 생성

    cnt = bfs(virus)  # bfs 탐색
    ans = max(ans, len(clean) - cnt)  # 미감염 최대값 계산

print(ans)

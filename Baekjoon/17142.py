from collections import deque
from copy import deepcopy
from itertools import combinations

# 0: 빈칸 1: 벽 2: 바이러스


def bfs(v: list, lab: list):

    for i, j in v:  # 시작점 초기화
        lab[i][j] = 0

    dq = deque(v)
    cnt = m

    while dq:
        r, c = dq.popleft()
        at = lab[r][c]  # 바이러스 최종 도착시간

        if lab[r][c] > ans[0]:  # 이미 최소값을 넘은 경우
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if lab[nr][nc] == -1:  # 이동가능할 경우
                    lab[nr][nc] = lab[r][c] + 1
                    cnt += 1
                    dq.append((nr, nc))

                if lab[nr][nc] == -2 and cnt != t:  # 이동가능할 경우
                    lab[nr][nc] = lab[r][c] + 1
                    dq.append((nr, nc))

    if cnt == t:  # 퍼진 바이러스 개수가 필요한 수를 충족했을 경우
        ans[0] = min(ans[0], at)


n, m = map(int, input().split())
mp = []
virus = []  # 바이러스 위치 저장
ans = [n**2+1]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

t = m  # 필요 이동 개수 초기화

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 0:  # 움직임 가능 표시
            t += 1
            line[j] = -1

        if line[j] == 2:  # 바이러스 표시
            virus.append((i, j))
            line[j] = -2

    mp.append(line)


for v in combinations(virus, m):
    bfs(v, deepcopy(mp))

if ans[0] == n**2+1:  # 변동이 없었을 경우
    ans[0] = -1

print(ans[0])

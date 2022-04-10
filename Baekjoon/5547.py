from collections import deque
from pprint import pprint


def bfs(x, y):

    dq = deque([[x, y]])
    visited[0][0] = 1  # 방문표시 초기화
    cnt = 0

    while dq:
        x, y = dq.popleft()

        if y % 2:  # y 홀수일 경우
            dx = [0, 1, -1, 1, 0, 1]
            dy = [-1, -1, 0, 0, 1, 1]
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w + 2 and 0 <= ny < h + 2:  # 이동가능 확인
                    if lst[ny][nx] == 1:  # 벽일 경우 개수 추가
                        cnt += 1
                    elif not visited[ny][nx]:  # 방문하지 않은 길일 경우 dq에 추가
                        visited[ny][nx] = 1
                        dq.append([nx, ny])

        else:  # y 짝수일 경우
            dx = [-1, 0, -1, 1, -1, 0]
            dy = [-1, -1, 0, 0, 1, 1]
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < w + 2 and 0 <= ny < h + 2:  # 이동가능 확인
                    if lst[ny][nx] == 1:  # 벽일 경우 개수 추가
                        cnt += 1
                    elif not visited[ny][nx]:  # 방문하지 않은 길일 경우 dq에 추가
                        visited[ny][nx] = 1
                        dq.append([nx, ny])

    return cnt


w, h = map(int, input().split())
lst = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]  # 주변에 길을 생성
lst = [[0] * (w + 2)] + lst + [[0] * (w + 2)]
visited = [[0] * (w + 2) for _ in range(h + 2)]  # 방문표시 초기화

ans = bfs(0, 0)

print(ans)

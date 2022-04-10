# 1. 문제 솔루션 코드를 작성합니다.

import heapq
from collections import defaultdict

ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m, k = map(int, input().split())
    res = [0]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    time_line = defaultdict(list)  # 시계열 순 분열세포의 위치,크기값을 저장합니다.
    visited = [[0] * 1000 for _ in range(1000)]  # 방문표시 저장(범위는 그냥 크게 만들었습니다)

    # 최대힙으로 높은 우선순위를 가진 세포(크키)순으로 분열지점에 저장합니다.
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j]:
                res[0] += 1
                visited[i + 500][j + 500] = 1  # 초기위치 지정
                heapq.heappush(time_line[line[j] + 1], (line[j] * (-1), i + 500, j + 500))

    t = 1  # 시간
    while t <= k:
        if time_line[t]:  # t시간에 분열세포가 있는 경우
            for cell in time_line[t]:  # 최대힙으로 높은 우선순위 순 탐색
                size, r, c = cell
                size *= -1

                if size + t - 1 <= k:  # 종료시점에 활성화되지 못하는 경우
                    res[0] -= 1

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if not visited[nr][nc]:  # 방문하지 않은 경우
                        res[0] += 1
                        visited[nr][nc] = 1
                        heapq.heappush(time_line[t + size + 1], (size * (-1), nr, nc))

        t += 1
    print(time_line)
    ans.append("#{} {}".format(test, res[0]))

print(*ans, sep="\n")

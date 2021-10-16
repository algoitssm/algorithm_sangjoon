from collections import deque, defaultdict

ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m, k = map(int, input().split())
    res = [0]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    time_line = defaultdict(list)
    used_cells = deque([])
    visited = []  # 사용위치 저장

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j]:
                visited.append((i, j))
                time_line[line[j]+1].append((i, j, line[j]))  # t, size 저장

    t = 1
    while t <= k:
        print(time_line)
        t += 1
        if time_line[t]:
            cells = sorted(time_line[t], key=lambda x: x[2])
            for cell in cells:
                r, c, size = cell

                if size - k > 1:
                    res[0] += 1

                # 상화좌우 순회하며
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (nr, nc) not in visited:
                        visited.append((nr, nc))
                        time_line[t + size + 1].append((nr, nc, size))

        # 사용세포
    res[0] += len(cells)
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")

# 카메라 방향으로 탐색하여 방문지점 및 개수 반환
def check_room(r, c, p):
    v = set()
    cnt = 0
    for i in p:
        tr, tc = r, c
        dr, dc = d[i]
        while 0 <= tr + dr < n and 0 <= tc + dc < m:
            tr += dr
            tc += dc
            if mp[tr][tc] == 6:
                break
            if (tr, tc) not in visited:
                cnt += 1
                v.add((tr, tc))
    return v, cnt


# 모든 카메라에 대해 순회하며 dfs 탐색


def dfs(idx):
    global visited
    if total - len(visited) == 0:  # 모든 카메라를 사용하기 이전에 사각지대가 없는 경우
        ans[0] = 0
        return

    if idx == tl:  # 모든 카메라 탐색
        ans[0] = min(ans[0], total - len(visited))
        return

    r, c = camera[idx]  # 카메라 위치
    c_no = mp[r][c]  # 카메라 번호

    for p in cd[c_no]:  # 카메라 탐색 방향에 대해 순회
        tmp_v, tmp_cnt = check_room(r, c, p)  # 카메라 탐색지점 및 개수 반환
        visited = visited | tmp_v
        dfs(idx + 1)  # 다음카메라 탐색
        visited = visited - tmp_v


# 입력
n, m = map(int, input().split())

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cd = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    5: [[0, 1, 2, 3]],
}

mp = []
camera = []
total = n * m  # 전체 삭각지대 개수
ans = [n * m]  # 정답 초기화

for i in range(n):
    line = list(map(int, input().split()))
    mp.append(line)
    for j in range(m):
        if 0 < line[j] < 6:
            camera.append((i, j))
        if line[j] == 6:
            total -= 1

visited = set(camera)
tl = len(camera)
dfs(0)
print(ans[0])

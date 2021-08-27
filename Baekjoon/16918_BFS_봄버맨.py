def bomber_man(t: int):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    if not t % 2:
        for i in range(r):
            for j in range(c):
                if lst[i][j] == "O":  # 기존 폭탄 확인
                    check.append((i, j))
                if lst[i][j] == ".":  # 폭탄 설치
                    lst[i][j] = "O"

    else:
        for x, y in check:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:  # 폭탄 폭발 처리
                    lst[nx][ny] = "."

        check.clear()  # 기존 폭탄 초기화


r, c, n = map(int, input().split())
lst = [list(input()) for _ in range(r)]
check = []


for t in range(1, n + 1):
    bomber_man(t)

for line in lst:
    print("".join(line))
test_case = int(input())
for tc in range(1, test_case + 1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n + 2)]
    mp = [[0] * (n + 2) for _ in range(n + 2)]

    # 연결 확인
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) <= 1000:
                mp[i][j] = 1

    # 플로이드 와샬
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if mp[i][k] and mp[k][j]:
                    mp[i][j] = 1

    if mp[0][n + 1]:
        print("happy")
    else:
        print("sad")

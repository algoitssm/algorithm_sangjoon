def check_time(stair: tuple, people: list):
    sr, sc = stair
    time = mp[sr][sc]
    l = [abs(pr-sr) + abs(pc-sc) + time + 1 for pr, pc in people]
    l.sort()

    # 도착순으로 정렬하였을 경우, 앞 3번째 사람만 벗어나면 계단에 진입이 가능
    # 그러므로 앞 3번째의 도착 시간 기준으로 기다려야하는 시간을 저장
    for i in range(3, len(l)):
        l[i] += l[i-3] - (l[i]-time) if l[i-3] - (l[i]-time) > 0 else 0

    return l[-1] if l else 0


ans = []
test_case = int(input())
for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]
    p, s = [], []
    cnt = float("inf")

    # 사람, 계단 위치 저장
    for i in range(n):
        for j in range(n):
            if mp[i][j] == 1:
                p.append((i, j))
            elif mp[i][j] != 0:
                s.append((i, j))

    # 비트마스킹을 활용하여 조합 생성
    for i in range(1 << len(p)):
        p1, p2 = [], []
        for j in range(len(p)):
            if i & (1 << j):
                p1.append(p[j])
            else:
                p2.append(p[j])

        t1 = check_time(s[0], p1)
        t2 = check_time(s[1], p2)
        cnt = min(cnt, max(t1, t2))
    ans.append("#{} {}".format(test, cnt))

print(*ans, sep="\n")

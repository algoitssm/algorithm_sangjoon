from collections import deque

ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n, m, k, wa, wb = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    tk = deque(map(int, input().split()))

    d = [[[0, 0]] * (n + 1), [[0, 0, 0]] * (m + 1)]
    q = [deque([]), deque([])]
    cnt = 0
    num = 0
    check = {}
    res = 0
    while len(check) < k:

        # 접수대기 배치
        while tk and tk[0] == cnt:
            tk.popleft()
            num += 1
            q[0].append(num)

        # 접수창구 배치
        tmp = []
        for i in range(1, n + 1):
            if d[0][i][1]:  # 창구에 사람이 있으면
                d[0][i][1] -= 1

            if not d[0][i][1]:  # 창구가 사용가능하다면
                if d[0][i][0]:  # 사람이 있다면
                    tmp.append((d[0][i][0], i))
                    d[0][i] = [0, 0]

                if q[0]:  # 대기열에 사람이 있다면
                    e = q[0].popleft()
                    d[0][i] = [e, a[i]]

        # 정비대기 배치
        tmp.sort(key=lambda x: x[1])
        for p, idx in tmp:
            q[1].append((p, idx))

        # 정비 배치
        for i in range(1, m + 1):
            p, idx, c = d[1][i]
            if d[1][i][2]:
                d[1][i][2] -= 1

            if not d[1][i][2]:  # 창구가 사용가능하다면
                if p:  # 사람이 있다면
                    check[p] = [idx, i]  # 최종 방문 지점 기록
                    d[1][i] = [0, 0, 0]
                if q[1]:  # 대기열에 사람이 있다면
                    tp, tidx = q[1].popleft()
                    d[1][i] = [tp, tidx, b[i]]

        cnt += 1

    for i, dest in check.items():
        if dest == [wa, wb]:
            res += i
    if not res:
        res = -1
    ans.append("#{} {}".format(test, res))

print(*ans, sep="\n")

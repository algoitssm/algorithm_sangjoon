from itertools import combinations


def build_film(n):
    if n >= ans:
        test_film()
        return

    change[com[n]] = 1
    build_film(n+1)

    change[com[n]] = 0
    build_film(n+1)

# 생성된 약품 조합에 따른 검사결과 반환


def test_film():
    global test
    for i in range(W):
        m, t = 1, 1
        for j in range(1, D):
            f = change[j-1] if j-1 in change else film[j-1][i]
            b = change[j] if j in change else film[j][i]

            if f == b:
                t += 1
            else:
                m = max(m, t)
                t = 1
        m = max(m, t)

        if m < K:
            return

    test = True


test = int(input())

for test_case in range(1, test+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    test = False
    ans = 0

    # 약품 개수에 따른 조합 생성
    while ans <= K:
        breaker = False
        combi = combinations([i for i in range(D)], ans)

        for com in combi:
            change = {}
            # 조합에 따른 필름 생성
            build_film(0)

            if test:
                breaker = True
                break

        if breaker:
            break
        ans += 1

    print(f"#{test_case} {ans}")

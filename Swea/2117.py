# 1. 문제 솔루션 코드를 작성합니다.


def get_cost(k):  # 비용 계산 함수
    return k**2 + (k - 1) ** 2


def count_house(r1, c1, k):  # 마름모 내 집 개수 확인
    cnt = 0
    for r2, c2 in h:
        if abs(r1 - r2) + abs(c1 - c2) <= k - 1:
            cnt += 1
    return cnt


def check_net(k):  # 이익 확인 및 최대 집 개수 확인: k가 클수록 많은 집을 확보가능
    cost = get_cost(k)

    for i in range(n):
        for j in range(n):
            cnt = count_house(i, j, k)
            net = cnt * m - cost
            if net >= 0 and cnt > res[0]:
                res[0] = cnt

    if res[0]:
        return True


ans = []
test = int(input())
for tc in range(1, test + 1):
    n, m = map(int, input().split())
    res = [0, 0, 0]

    # 집위치 저장
    h = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j]:
                h.append((i, j))

    for k in range(n + 2, 0, -1):  # 방범 최대 크기기준 순회
        if check_net(k):
            break

    ans.append("#{} {}".format(tc, res[0]))

print(*ans, sep="\n")

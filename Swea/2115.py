from itertools import combinations


# 최대 벌꿀 값 반환
def get_honey(lst):
    honey = 0
    for i in range(1, M+1):
        combi = combinations(lst, i)
        for com in combi:
            if sum(com) <= C:
                honey = max(honey, sum(map(lambda x: x**2, com)))
    return honey


test = int(input())
for test_case in range(1, test+1):
    N, M, C = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 일꿀 1 지정
    for i in range(N):
        for j in range(N-M+1):
            o = mp[i][j:j+M]
            # 일꾼 2 지정
            for k in range(N):
                for l in range(N-M+1):
                    # 동선이 겹치는 경우
                    if k == i and (j <= l < j+M or j <= l+M-1 < j+M):
                        continue
                    t = mp[k][l:l+M]

                    ans = max(ans, get_honey(o)+get_honey(t))

    print(f"#{test_case} {ans}")

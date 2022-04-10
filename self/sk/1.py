from collections import defaultdict

M = [1, 5, 10, 50, 100, 500]


def solution(money, costs):
    answer = 0
    lst = [[] for _ in range(6)]

    for i, c in enumerate(costs):
        for j in range(i, 6):
            lst[i].append(M[j] // M[i] * c)

    for i in reversed(range(6)):
        tmp = float("inf")
        d, money = divmod(money, M[i])

        for j in range(i + 1):
            c = lst[j].pop()
            tmp = min(tmp, c)

        answer += d * tmp

    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000]))

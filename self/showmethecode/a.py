from collections import defaultdict, deque

answer = [float("inf")]
dct = defaultdict(list)
n = int(input())
price = [0] + list(map(int, input().split()))
v = [0] * (n + 1)

for i in range(n):
    m = int(input())
    for _ in range(m):
        a, s = map(int, input().split())
        dct[i + 1].append([a, s])


def dfs(cost):
    global price

    if cost >= answer[0]:
        return

    if sum(v) == n:
        print(cost, v, price)
        answer[0] = cost

    for i in range(1, n + 1):
        if not v[i]:
            v[i] = 1
            tmp = price[::]
            for a, c in dct[i]:
                price[a] = max(1, price[a] - c)
            dfs(cost + price[i])
            price = tmp
            v[i] = 0


dfs(0)
print(answer[0])

from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    tr = defaultdict(list)

    for a, b in edge:
        tr[a].append(b)
        tr[b].append(a)

    v = [0] * (n + 1)
    v[1] = 1
    dq = deque([1])

    while dq:
        s = dq.popleft()

        for e in tr[s]:
            if not v[e]:
                v[e] = v[s] + 1
                dq.append(e)
    t = max(v)
    answer = v.count(t)
    print(v)
    return answer

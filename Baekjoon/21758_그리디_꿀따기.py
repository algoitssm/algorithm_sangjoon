from collections import deque


def count_a_to_b(a, b):
    dq = deque([(a, 1)])

    while dq:
        e, cnt = dq.popleft()
        if e == b:
            return cnt

        if e > b:
            continue

        dq.append((e * 2, cnt + 1))
        dq.append((e * 10 + 1, cnt + 1))
        print(dq)
    return -1


a, b = map(int, input().split())
ans = count_a_to_b(a, b)
print(ans)

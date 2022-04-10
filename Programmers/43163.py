from collections import deque


def is_possible(a, b):
    cnt = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    if cnt == 1:
        return True

    return False


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    dq = deque([(begin, 0)])
    v = [0] * len(words)

    while dq:
        b, cnt = dq.popleft()

        for i in range(len(words)):
            if not v[i]:
                t = words[i]
                if is_possible(b, t):
                    if t == target:
                        return cnt + 1
                    dq.append((t, cnt + 1))
                    v[i] = 1

    return answer

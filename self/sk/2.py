from pprint import pprint


def solution(n, clockwise):
    h = n // 2
    e = h**2 + h + 1 if n % 2 else h**2
    answer = [[e] * n for _ in range(n)]
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

    r1, c1 = 0, -1
    r2, c2 = -1, n - 1
    r3, c3 = n - 1, n
    r4, c4 = n, 0

    cnt = 0
    for i in range(h):
        for j in range((n - 1) - i * 2, 0, -1):
            cnt += 1
            r1, c1 = r1 + dr[i % 4], c1 + dc[i % 4]
            r2, c2 = r2 + dr[(i + 1) % 4], c2 + dc[(i + 1) % 4]
            r3, c3 = r3 + dr[(i + 2) % 4], c3 + dc[(i + 2) % 4]
            r4, c4 = r4 + dr[(i + 3) % 4], c4 + dc[(i + 3) % 4]

            answer[r1][c1] = cnt
            answer[r2][c2] = cnt
            answer[r3][c3] = cnt
            answer[r4][c4] = cnt

    if not clockwise:
        answer = answer[::-1]

    return answer


pprint(solution(5, True))
pprint(solution(5, False))

# pprint(solution(6, True))
# pprint(solution(9, True))

from math import factorial


def solution(width, height, diagonals):
    answer = 0
    w, h = width, height
    t = w + h

    for x, y in diagonals:
        r1, c1 = x, y - 1
        r2, c2 = x - 1, y

        answer += (
            factorial(r1 + c1)
            // (factorial(r1) * factorial(c1))
            * factorial(t - r2 - c2)
            // (factorial(w - r2) * factorial(h - c2))
        )
        answer += (
            factorial(r2 + c2)
            // (factorial(r2) * factorial(c2))
            * factorial(t - r1 - c1)
            // (factorial(w - r1) * factorial(h - c1))
        )

    return answer % 10000019


print(solution(2, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))


# from collections import deque

# def solution(width, height, diagonals):
#     answer = 0
#     dr = [1, 0]
#     dc = [0, 1]

#     mp = [[0]*(width+1) for _ in range(height+1)]
#     v = [[0]*(width+1) for _ in range(height+1)]

#     for x, y in diagonals:
#         mp[y][x-1], mp[y-1][x] = -1, 1

#     dq = deque([(0,0,0)])

#     while dq:
#         r,c,t = dq.popleft()

#         if r and c and t:
#             answer += 1
#             continue

#         for i in range(2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0<= nr <= height and 0<= nc <= width:
#                 dq.append((nr, nc, t))

#         if not t and mp[r][c]:
#             if mp[r][c] == 1:
#                 nr, nc = r+1 ,c-1
#             elif mp[r][c] == -1:
#                 nr, nc = r-1, c+1

#             if 0<= nr <= height and 0<= nc <= width:
#                 dq.append((nr, nc ,1))

#     return answer

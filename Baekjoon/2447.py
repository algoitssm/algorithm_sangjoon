import sys


def dfs(sx, ex, sy, ey):

    p = (ex - sx) // 3  # 중단점 설정

    if not p:
        return

    # 중앙 제외 부분 재귀
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                dfs(sx + (p * i), sx + (p * (i + 1)), sy + (p * j), sy + (p * (j + 1)))

    # 중앙 부분 체크
    for i in range(sx + p, sx + (p * 2)):
        mp[i][sy + p : sy + (p * 2)] = [" "] * p


sys.setrecursionlimit(10**9)
k = int(input())

mp = [["*"] * k for _ in range(k)]
dfs(0, k, 0, k)

for line in mp:
    print("".join(line))

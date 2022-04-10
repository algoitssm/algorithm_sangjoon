def dfs(n):
    visited[n] = True
    for com in link:  # n과 연결되어있을 경우
        if com[0] == n and visited[com[1]] == False:
            dfs(com[1])
        if com[1] == n and visited[com[0]] == False:
            dfs(com[0])

    return


from sys import stdin

n = int(input())
l = int(input())

link = [list(map(int, stdin.readline().split())) for _ in range(l)]
visited = [False] * (n + 1)  # 방문 표시

dfs(1)  # 1과 연결되어있을 경우

print(visited.count(True) - 1)

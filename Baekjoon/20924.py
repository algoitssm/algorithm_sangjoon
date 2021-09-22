

# def get_giga(r: int):

#     visited[r] = True
#     # 루트노드가 기가노트일 경우
#     if len(tree[r]) != 1:
#         get_max_branch(r, 0)
#         return 0

#     giga, root_length = tree[r][0][0], tree[r][0][1]

#     while True:
#         visited[giga] = True

#         # 기가노드 판별
#         if len(tree[giga]) != 2:
#             break

#         for node, length in tree[giga][1:]:
#             if not visited[node]:
#                 root_length += length
#                 giga = node

#     get_max_branch(giga, 0)
#     return root_length


# def get_max_branch(giga: int, length: int):
#     global max_branch
#     # 리프노드일 경우 최대값 판별
#     if len(tree[giga]) == 1:
#         max_branch = max(max_branch, length)

#     for node, line in tree[giga]:
#         if not visited[node]:
#             visited[node] = True
#             get_max_branch(node, length+line)

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

ans = [0, 0]


def dfs(cur, par, length, check):

    # 루트 노드일 경우
    if not check:
        ans[0] = length
    # 가지노드일 경우
    else:
        ans[1] = max(ans[1], length)

    # 기가노드 판별
    if not check and len(tree[cur]) > 2 - int(cur == r):
        length, check = 0, 1

    # 가지노드 dfs 탐색
    for node, line in tree[cur]:
        if not node == par:
            dfs(node, cur, length+line, check)


dfs(r, r, 0, 0)
print(ans[0], ans[1])

# def find(parent, x):
#     if parent[x] != x:
#         return find(parent, parent[x])
#     return x

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

#     return parent

# def solution(n, edges):
#     answer = 0
#     parent = [i for i in range(n)]

#     for a, b in edges:
#         if find(parent, a) == find(parent, b):

#         parent = union(parent, a, b)

#     print(parent)

#     return answer

# solution(5, [[0,1],[0,2],[1,3],[1,4]])


def solution(n, edges):
    answer = 2 ** (n - 1)
    return answer

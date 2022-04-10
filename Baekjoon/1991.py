from sys import stdin


def preorder_traverse(node: str):

    print(node, end="")

    if graph[node][0] != ".":
        preorder_traverse(graph[node][0])

    if graph[node][1] != ".":
        preorder_traverse(graph[node][1])


def inorder_traverese(node):
    if graph[node][0] != ".":
        inorder_traverese(graph[node][0])
    print(node, end="")

    if graph[node][1] != ".":
        inorder_traverese(graph[node][1])


def postorder_traverse(node):

    if graph[node][0] != ".":
        postorder_traverse(graph[node][0])

    if graph[node][1] != ".":
        postorder_traverse(graph[node][1])

    print(node, end="")


n = int(input())
graph = {}

for _ in range(n):
    p, s1, s2 = input().split()
    graph[p] = [s1, s2]

preorder_traverse("A")
print()
inorder_traverese("A")
print()
postorder_traverse("A")

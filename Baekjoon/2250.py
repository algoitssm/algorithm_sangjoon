import sys

input = sys.stdin.readline


n = int(input())
# 트리 생성
tree = [[0] for _ in range(n+1)]
for _ in range(n):
    a, l, r = map(int, input().split())
    tree[a].extend([l, r])
    if l != -1:
        tree[l][0] = a
    if r != -1:
        tree[r][0] = a

for i in range(1, n+1):
    if tree[i][0] == 0:
        root = i


# 중위 탐색
level_dic = {}
cnt = 0


def in_order_traverse(node: int, level: int):
    global cnt

    # 왼쪽
    if tree[node][1] != -1:
        in_order_traverse(tree[node][1], level+1)

    # 노드의 레벨 기준 위치 지정
    cnt += 1
    if not level in level_dic:
        level_dic[level] = [cnt, - (n + 1)]
    else:
        level_dic[level][1] = cnt
    # 오른쪽
    if tree[node][2] != -1:
        in_order_traverse(tree[node][2], level+1)


in_order_traverse(root, 1)
sort_lst = sorted(level_dic.items(),
                  key=lambda x: (-(x[1][1]-x[1][0]), x[0]))
ans = [sort_lst[0][0], sort_lst[0][1][1] - sort_lst[0][1][0] + 1]

if ans[1] <= 0:
    ans = [1, 1]

print(ans[0], ans[1])


#####
# 클래스를 활용한 트리 탐색에 대해 검색하다 찾은 코드
# 클래스와 비트마스킹을 활용한 루트노드 찾는 방법에 대해 공부 필요
#####
# import math

# class Node:
#     def __init__(self, parent, leftNode, rightNode, level, x):
#         self.parent = parent
#         self.leftNode = leftNode
#         self.rightNode = rightNode
#         self.level = level
#         self.x = x

# # 중위 순회
# def inOrder(node, level):
#     global x
#     if node.leftNode != None:
#         node.level = level
#         inOrder(tree[node.leftNode], level+1)
#     node.level = level
#     node.x = x
#     x += 1
#     if node.rightNode != None:
#         inOrder(tree[node.rightNode], level+1)

# n = int(sys.stdin.readline().rstrip())
# tree = {}
# root = (1<<(n+1))-2 # 비트마스킹으로 루트노드 찾기 n=5, 111110
# for _ in range(n):
#     parent, leftNode, rightNode = map(int, sys.stdin.readline().rstrip().split())

#     # 루트노드 찾기
#     if leftNode > 0:
#         root &= ~(1<<leftNode)
#     if rightNode > 0:
#         root &= ~(1<<rightNode)

#     if leftNode == -1:
#         leftNode = None
#     if rightNode == -1:
#         rightNode = None
#     tree[parent] = Node(parent, leftNode, rightNode, 0, 0)

# root = int(math.log(root, 2)) # 루트노드
# x = 1 # 노드의 x좌표
# inOrder(tree[root],1)

# order = sorted(tree.keys() , key = lambda x : tree[x].level) # 트리 레벨 순으로 정렬
# data = []
# ans = [1,1] # level, width
# for i in range(1, n):
#     # 트리 레벨이 달라지면 그동안 data배열에 넣었던 x좌표들의 최댓값-최소값+1 = 너비 구해서 비교
#     if tree[order[i]].level != tree[order[i-1]].level:
#         if len(data) > 1:
#             width = max(data) - min(data) + 1
#             if ans[1] < width:
#                 ans[0] = tree[order[i-1]].level
#                 ans[1] = width
#         data = []
#     data.append(tree[order[i]].x)
# if len(data) > 1:
#     width = max(data) - min(data) + 1
#     if ans[1] < width:
#         ans[0] = tree[order[i-1]].level
#         ans[1] = width

# print(*ans)

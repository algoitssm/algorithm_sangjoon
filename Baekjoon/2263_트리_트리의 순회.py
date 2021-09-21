import sys


def get_preorder(in_start: int, in_end: int, post_start: int, post_end: int):

    if in_start > in_end or post_start > post_end:
        return

    parent_node = postorder[post_end]
    print(parent_node, end=" ")

    parent_idx = inorder.index(parent_node)  # 3

    get_preorder(in_start, parent_idx-1, post_start, parent_idx-1)
    get_preorder(parent_idx+1, in_end, parent_idx, post_end-1)


sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

get_preorder(0, n-1, 0, n-1)


# 1 2 4 5 3 6 7
# 7
# 4 2 5 1 6 3 7
# 4 5 2 6 7 3 1
# 0 1 2 3 4 5 6

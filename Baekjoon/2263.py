import sys


def get_preorder(in_start: int, in_end: int, post_start: int, post_end: int):

    if in_start <= in_end and post_start <= post_end:

        parent_node = postorder[post_end]
        print(parent_node, end=" ")

        parent_idx = post_idx[parent_node]  # 3
        left = parent_idx - in_start  # 왼쪽인자 갯수
        right = in_end - parent_idx

        get_preorder(in_start, parent_idx - 1, post_start, post_start + left - 1)
        get_preorder(parent_idx + 1, in_end, post_end - right, post_end - 1)


sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 인덱싱 저장
post_idx = [0] * (n + 1)
for i in range(n):
    post_idx[inorder[i]] = i

get_preorder(0, n - 1, 0, n - 1)

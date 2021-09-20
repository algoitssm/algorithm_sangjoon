def get_postorder(inorder: list):

    # 리프 노드일 경우
    if not len(inorder):
        return

    # 최상위 루트노드 기준으로 아래 노드를 내려가며 탐색
    root_node = preorder.pop(0)
    root_idx = inorder.index(root_node)

    left_inorder = inorder[:root_idx]
    get_postorder(left_inorder)

    right_indorder = inorder[root_idx+1:]
    get_postorder(right_indorder)

    # 최하위의 노드부터 위로 올라가며 탐색
    ans.append(root_node)


T = int(input())

for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    ans = []
    get_postorder(inorder)

    print(" ".join(map(str, ans)))

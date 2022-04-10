from collections import deque


def make_tree(tree_lst: list):
    tree = {}

    for i in range(0, len(tree_lst), 2):
        u, v = tree_lst[i], tree_lst[i + 1]
        # 자식노드 생성
        if u in tree:
            tree[u].append(v)
        else:
            tree[u] = [0, v]

        # 부모 노드 체크
        if v in tree:
            # 부모노드가 이미 있을 경우 (두개의 부모노드를 가지는 경우)
            if tree[v][0] != 0:
                return False
            else:
                tree[v][0] = u
        else:
            tree[v] = [u]

    return tree


def is_tree(tree: dict):
    visited = {}
    root = -1

    # 루트노드 탐색과 방문표시 초기화
    for k, v in tree.items():
        visited[k] = False
        if v[0] == 0:
            root = k

    if root == -1:
        return False

    dq = deque([root])

    # 루트노드 기준 완전 탐색
    while dq:
        e = dq.popleft()
        visited[e] = True

        # 자식노드가 있는 경우
        if len(tree[e]) > 1:
            for node in tree[e][1:]:
                dq.append(node)

    for _, v in visited.items():  # 루트노드가 2가지 이상인 경우 탐색
        if not v:
            return False

    return True


def check_tree(lst: list):
    # 빈 리스트일 경우
    if not lst:
        print(f"Case {case} is a tree.")
        return

    # 트리 생성
    tree = make_tree(lst)

    # 트리가 아닐 경우
    if not tree:
        print(f"Case {case} is not a tree.")
    else:
        if is_tree(tree):
            print(f"Case {case} is a tree.")
        else:
            print(f"Case {case} is not a tree.")


lst = []
case = 1
while True:

    temp = list(map(int, input().split()))
    lst += temp

    # 모든 Case 가 끝난 경우
    if temp and lst[-1] < 0 and lst[-2] < 0:
        break

    # Case 입력이 끝난 경우
    elif temp and lst[-1] == 0 and lst[-1] == 0:
        lst = lst[:-2]
        check_tree(lst)

        # 케이스 초기화
        lst = []
        case += 1

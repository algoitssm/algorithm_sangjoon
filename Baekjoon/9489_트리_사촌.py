from sys import stdin
import heapq

input = stdin.readline


def get_tree(root_node: int, lst: list):
    heap = [root_node]

    # 자식이 없는 노드 중 가장 작은 수를 가지는 노드의 자식순 순회
    while heap:
        parent_node = heapq.heappop(heap)

        # 리프노드일 경우
        if not lst:
            continue

        # 연속된 수 증감판단
        asc = 1 if len(lst) > 1 and lst[0] + 1 == lst[1] else -1

        # 연속되는 수까지 트리 생성 및 새로운 노드 힙에 추가
        while lst:
            e = lst.pop(0)
            tree[parent_node].append(e)
            tree[e] = [parent_node]
            heapq.heappush(heap, e)

            if not lst or e != lst[0] - asc:
                break


def get_cousin(n: int, root: int):
    cnt = 0

    # 부모 노드
    parent_node = tree[n][0]

    # 부모노드가 루트 노드일 경우
    if parent_node == root:
        return cnt

    # 부모의 형제의 자식들 계산
    grand_parent = tree[parent_node][0]
    for parent_sibling in tree[grand_parent][1:]:
        if parent_sibling != parent_node:
            cnt += len(tree[parent_sibling][1:])

    return cnt


while True:
    n, k = map(int, input().split())

    # 종료 조건
    if n == 0 and k == 0:
        break

    lst = list(map(int, input().split()))
    root = lst[0]
    # 트리 초기화
    tree = {root: [root]}
    get_tree(lst[0], lst[1:])
    print(get_cousin(k, root))

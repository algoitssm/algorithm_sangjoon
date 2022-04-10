from collections import deque

# bfs 탐색

n = int(input())
lst = list(map(int, input().split()))
cnt = (len(lst) + 1) // 2
prev = cnt
dq = deque([(cnt - 1, cnt)])

while dq:
    idx, cnt = dq.popleft()
    if cnt != prev:
        prev = cnt
        print()

    print(lst[idx], end=" ")
    cnt //= 2
    if cnt:
        dq.append((idx - cnt, cnt))
        dq.append((idx + cnt, cnt))


# def preorder_traverse(gh: lst, cnt):

#     if len(gh) == 1:
#         ans.append(ans.append((gh[0], cnt)))
#     if gh:
#         mid = len(gh) // 2
#         ans.append((gh[mid], cnt))

#         preorder_traverse(gh[:mid], cnt + 1)
#         preorder_traverse(gh[mid + 1 :], cnt + 1)


# n = int(input())
# lst = list(map(int, input().split()))
# ans, cnt = [], 0

# preorder_traverse(lst, cnt)

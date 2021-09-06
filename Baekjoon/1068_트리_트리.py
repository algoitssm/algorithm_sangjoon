def dfs(n: int):
    global cnt

    # 삭제 노드일 경우
    if n == cut:
        # 삭제된 노드의 부모노드가 하나의 자식노드를 가질 경우
        if tr[n] != -1 and len(gh[tr[n]]) == 1:
            cnt += 1
        return

    # 리프노드일 경우
    if not gh[n]:
        cnt += 1

    # 자식 노드가 있을 경우
    else:
        for node in gh[n]:
            dfs(node)


n = int(input())
tr = list(map(int, input().split()))
cut = int(input())

# 시작점 리프노드 초기화
s, cnt = 0, 0
gh = {i: [] for i in range(n)}

# 자식노드기준 그래프 생성
for idx, parent in enumerate(tr):
    if parent == -1:  # 시작지점 탐색
        s = idx
    else:
        gh[parent].append(idx)

dfs(s)
print(cnt)
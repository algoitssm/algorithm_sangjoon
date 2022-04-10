n, m = map(int, input().split())

store = int(input())
lst = [tuple(map(int, input().split())) for _ in range(store)]

cur, cur_l = map(int, input().split())
ans = 0
side = [(1, 2), (2, 1), (3, 4), (4, 3)]

for d, l in lst:
    if cur == d:  # 같은 방향일 경우
        ans += abs(cur_l - l)

    if (cur_l, l) in side:  # 반대편에 위치한 경우
        if d == 1 or d == 3:
            ans += m + min(cur_l + l, 2 * n - cur_l - l)
        else:
            ans += n + min(cur_l + l, 2 * m - cur_l - l)

    # 북
    if cur == 1 and d == 3:
        ans += cur_l + l
    if cur == 1 and d == 4:
        ans += (n - cur_l) + l
    # 남
    if cur == 2 and d == 3:
        ans += cur_l + (m - l)
    if cur == 2 and d == 4:
        ans += (n - cur_l) + (m - l)
    # 서
    if cur == 3 and d == 1:
        ans += cur_l + l
    if cur == 3 and d == 2:
        ans += (m - cur_l) + l
    # 동
    if cur == 4 and d == 1:
        ans += cur_l + (n - l)
    if cur == 4 and d == 2:
        ans += (m - cur_l) + (n - l)

print(ans)

def check(x1, x2, y1, y2):
    temp = 0

    for i in range(x1, x2):
        temp += sum(mp[i][y1:y2])

    if temp == 0:
        return 0
    elif temp == (x2 - x1) ** 2:
        return 1
    else:
        return 2


def divide(x1, x2, y1, y2):
    chk = check(x1, x2, y1, y2)

    if chk == 0:
        ans[0] += 1
    elif chk == 1:
        ans[1] += 1
    else:
        mx = (x2 - x1) // 2 + x1
        my = (y2 - y1) // 2 + y1
        divide(x1, mx, y1, my)
        divide(x1, mx, my, y2)
        divide(mx, x2, y1, my)
        divide(mx, x2, my, y2)


n = int(input())

mp = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]
divide(0, n, 0, n)
print("\n".join(map(str, ans)))

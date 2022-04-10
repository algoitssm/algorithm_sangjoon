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
        print("0", end="")
    elif chk == 1:
        print("1", end="")
    else:
        mx = (x2 - x1) // 2 + x1
        my = (y2 - y1) // 2 + y1
        print("(", end="")
        divide(x1, mx, y1, my)
        divide(x1, mx, my, y2)
        divide(mx, x2, y1, my)
        divide(mx, x2, my, y2)
        print(")", end="")


n = int(input())

mp = [list(map(int, list(input()))) for _ in range(n)]
divide(0, n, 0, n)

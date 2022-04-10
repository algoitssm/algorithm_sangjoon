def cnn(x1, x2, y1, y2):
    tmp = []

    if x2 - x1 == 2:
        for i in range(x1, x2):
            tmp.extend(mp[i][y1:y2])
        return sorted(tmp)[-2]

    mx = (x2 - x1) // 2 + x1
    my = (y2 - y1) // 2 + y1
    tmp.append(cnn(x1, mx, y1, my))
    tmp.append(cnn(x1, mx, my, y2))
    tmp.append(cnn(mx, x2, y1, my))
    tmp.append(cnn(mx, x2, my, y2))

    return sorted(tmp)[-2]


n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
print(cnn(0, n, 0, n))

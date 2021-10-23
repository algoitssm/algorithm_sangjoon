# 플루이드 와샬
gp = [[0]*58 for _ in range(58)]
n = int(input())
cnt = 0

for _ in range(n):
    a, _, b = input().split()

    if a == b:
        continue

    if not gp[ord(a)-65][ord(b)-65]:
        gp[ord(a)-65][ord(b)-65] = 1
        cnt += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i == j or gp[i][j]:
                continue

            if gp[i][k] and gp[k][j]:
                gp[i][j] = 1
                cnt += 1

print(cnt)
for i in range(58):
    for j in range(58):
        if gp[i][j]:
            print(f"{chr(i+65)} => {chr(j+65)}")

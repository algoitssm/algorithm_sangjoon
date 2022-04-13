n = input()
n = n if len(n) != 1 else "0" + n

ans = 1
tmp = n

while True:
    tmp = tmp[-1] + str(sum(map(int, tmp)))[-1]
    if tmp == n:
        break
    ans += 1

print(ans)

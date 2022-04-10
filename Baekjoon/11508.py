n = int(input())

lst = [int(input()) for _ in range(n)]

lst.sort(reverse=True)

ans = 0
for idx, cost in enumerate(lst):

    if idx % 3 != 2:
        ans += cost


print(ans)

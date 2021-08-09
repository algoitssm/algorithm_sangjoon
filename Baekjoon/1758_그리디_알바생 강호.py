n = int(input())

lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

ans = 0

for rank, tip in enumerate(lst):
    tip -= rank
    if tip > 0:
        ans += tip

print(ans)
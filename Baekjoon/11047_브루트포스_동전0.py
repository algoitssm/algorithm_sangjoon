n, k = map(int, input().split())

money_lst = [int(input()) for _ in range(n)]
money_lst.reverse()

cnt = 0

for money in money_lst:
    cnt += k // money
    k = k % money

print(cnt)

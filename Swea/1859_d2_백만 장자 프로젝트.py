test = int(input())

for i in range(1, test + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()

    ans = 0
    max_price = 0

    for price in lst:
        if price > max_price:
            max_price = price
        else:
            ans += max_price - price

    print(f"#{i} {ans}")

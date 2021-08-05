test = int(input())

for t in range(1, test + 1):
    lst = list(map(int, input().split()))
    lst.sort()
    ans = round(sum(lst[1:-1]) / 8)
    print(f"#{t} {ans}")

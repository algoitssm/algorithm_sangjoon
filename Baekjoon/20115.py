n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)

l = len(lst)

ans = lst[0] + sum(lst[1:]) / 2
print(ans)
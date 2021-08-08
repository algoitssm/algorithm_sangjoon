lst = set(range(1, 10001))
not_self_numbers = set()

for n in lst:
    not_self_number = n

    while n > 0:
        n, nums = divmod(n, 10)
        not_self_number += nums

    not_self_numbers.add(not_self_number)

ans = sorted(lst - not_self_numbers)
print("\n".join(map(str, ans)))
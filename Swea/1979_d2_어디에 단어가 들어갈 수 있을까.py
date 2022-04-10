test = int(input())

for t in range(1, test + 1):

    n, k = map(int, input().split())
    mapping = (
        [[0] * (n + 2)]
        + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
        + [[0] * (n + 2)]
    )

    reversed_mapping = list(map(list, zip(*mapping)))

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j + k <= n + 1:
                if sum(mapping[i][j : j + k]) == k:
                    if mapping[i][j - 1] == 0 and mapping[i][j + k] == 0:
                        ans += 1

            if i + k <= n + 1:
                if sum(reversed_mapping[j][i : i + k]) == k:
                    if reversed_mapping[j][i - 1] == 0 and reversed_mapping[j][i + k] == 0:
                        ans += 1

    print(f"#{t} {ans}")

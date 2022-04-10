test = int(input())


def check_airstrip(lst: list):
    check = [1] * N
    for i in range(N):
        stack = [lst[i][0]]
        up = None
        for j in range(1, N):
            if stack[-1] + 1 == lst[i][j]:  # 높아질 경우
                if up is None:
                    up = True

                else:
                    if len(stack) < X:
                        check[i] = 0
                        break
                    else:
                        stack = [lst[i][j]]
                        up = True

            elif stack[-1] - 1 == lst[i][j]:  # 낮아질 경우
                if up is False:
                    if len(stack) < X:
                        check[i] = 0
                        break
            elif stack[-1] == lst[i][j]:  # 같을 경우
                stack.append(lst[i][j])
            else:
                check[i] = 0
    print(check)
    return sum(check)


for test_case in range(1, test + 1):
    N, X = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    reversed_mp = list(map(list, zip(*mp)))
    ans += check_airstrip(mp)
    ans += check_airstrip(reversed_mp)
    print(f"#{test_case} {ans}")

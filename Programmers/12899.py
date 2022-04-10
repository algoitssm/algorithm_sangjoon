def to_elice(n):
    lst = ["1", "2", "4"]

    if n <= 3:
        return lst[n - 1]

    else:
        d, m = divmod(n - 1, 3)
        return solution(d) + lst[m]


def solution(n):
    answer = to_elice(n)
    return answer

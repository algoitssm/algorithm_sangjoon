# 유클리드 호재법
def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    answer = 1
    gcd = get_gcd(w, h)
    answer = w*h - (w + h - gcd)
    return answer


print(solution(8, 12))

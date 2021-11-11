# 유클리드 호재법
def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    answer = 1
    gcd = get_gcd(w, h)
    # 최대 공약수가 1인 경우
    if gcd == 1:
        answer = w*h - (w + h - 1)
    # 최대 공약수가 1이 아닌 경우
    else:
        answer = w*h - (w + h - gcd)
    return answer


print(solution(8, 12))

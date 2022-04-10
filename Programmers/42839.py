import math
from itertools import permutations


def check(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    answer = 0

    lst = set()

    for i in range(len(numbers)):
        for perm in permutations(numbers, i + 1):
            num = int("".join(perm))
            if num not in lst:
                if check(num):
                    lst.add(num)
                    answer += 1

    return answer


print(solution("011"))

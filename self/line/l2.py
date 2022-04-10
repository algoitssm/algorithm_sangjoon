from collections import Counter, defaultdict
from itertools import combinations


def solution(sentences, n):
    answer = -1
    cnt = 0
    dic = defaultdict(int)

    for sentence in sentences:
        word = Counter(sentence)
        alpha = set()
        shift = 0
        for letter in word.keys():
            if letter == " ":
                continue
            if letter.isupper():
                shift += 1
            alpha.add(letter.lower())

        if shift:
            alpha.add("-")

        if len(alpha) > n:
            continue

        score = len(sentence) + shift if shift else len(sentence)

        for comb in combinations(set(map(chr, range(97, 123))) | set("-"), n):
            if not alpha - set(comb):
                key = "".join(sorted(list(comb)))
                dic[comb] += score

        for score in dic.values():
            if score > answer:
                answer = score

    return answer


print(solution((["line in line", "LINE", "in lion"]), 5))

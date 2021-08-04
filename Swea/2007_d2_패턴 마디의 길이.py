from unittest import result


test = int(input())


def check_pattern(text: str):
    ans = 0
    for i in range(1, 11):
        case = 30 // i
        check = True
        pattern = text[:i]

        for j in range(1, case):
            if pattern != text[i * j : i * (j + 1)]:
                check = False
                break

        if check:
            return i

    return ans


for t in range(1, test + 1):
    text = input()
    ans = check_pattern(text)
    print(f"#{t} {ans}")
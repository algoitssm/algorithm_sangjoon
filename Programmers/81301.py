dic = {
    "": "",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(s):
    answer = ""
    tmp = ""

    for w in s:
        try:
            num = int(w)
            answer += dic[tmp]
            answer += str(w)
            tmp = ""
            continue

        except:
            if tmp in dic:
                answer += dic[tmp]
                tmp = ""
            tmp += w

    answer += dic[tmp]

    return int(answer)

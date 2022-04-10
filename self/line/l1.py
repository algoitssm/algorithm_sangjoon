def solution(logs):
    answer = 0
    keys = ["team_name", "application_name", "error_level", "message"]

    for log in logs:
        if len(log) > 100:
            answer += 1
            continue

        lst = log.split(" ")
        if len(lst) != 12:
            answer += 1
            continue

        chk = False
        print(lst)
        for i in range(12):
            word = lst[i]
            if i % 3 == 0 and word not in keys:
                chk = True
                break
            if i % 3 == 1 and word != ":":
                chk = True
                break

            if i % 3 == 2:
                if len(word.split(" ")) > 1 or not word.isalpha():
                    chk = True
                    break
        if chk:
            answer += 1
            continue

    return answer


print(
    solution(
        [
            "team_name : db application_name : dbtest error_level : info message : test",
        ]
    )
)

from collections import defaultdict


def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = set()
    v = [0] * (num_teams + 1)
    dic = defaultdict(list)
    office_set = set(office_tasks)

    for idx, employ in enumerate(employees):
        lst = employ.split(" ")
        team, task = int(lst[0]), set(lst[1:])
        employ_id = idx + 1

        dic[team].append(employ_id)
        if office_set & task:
            v[team] = 1
            continue

        else:
            answer.add(employ_id)

    for i in range(1, num_teams + 1):
        if not v[i]:
            answer = answer - set([dic[i][0]])

    return list(answer)


print(
    solution(
        3,
        ["development", "marketing", "hometask"],
        ["recruitment", "education", "officetask"],
        [
            "1 development hometask",
            "1 recruitment marketing",
            "2 hometask",
            "2 development marketing hometask",
            "3 marketing",
            "3 officetask",
            "3 development",
        ],
    )
)

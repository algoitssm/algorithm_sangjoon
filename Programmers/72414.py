def str_to_int(t: str):
    [h, m, s] = t.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(t: int):
    h, tmp = str(t // 3600).zfill(2), t % 3600
    m, s = str(tmp // 60).zfill(2), str(tmp % 60).zfill(2)
    return ":".join([h, m, s])


def solution(play_time, adv_time, logs):
    answer = 0
    advt = str_to_int(adv_time)
    pt = str_to_int(play_time)

    timeline = [0] * (pt + 1)

    for t in logs:
        st, et = t.split("-")
        s, e = str_to_int(st), str_to_int(et)
        timeline[s] += 1
        timeline[e] -= 1

    for i in range(1, pt + 1):
        timeline[i] = timeline[i] + timeline[i - 1]

    for i in range(1, pt + 1):
        timeline[i] = timeline[i] + timeline[i - 1]

    max_view = timeline[advt - 1]

    for i in range(0, pt - advt):
        tmp_mv = timeline[i + advt] - timeline[i]

        if tmp_mv > max_view:
            max_view, answer = tmp_mv, i + 1

    return int_to_str(answer)


print(
    solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30",
        ],
    )
)
print(
    solution(
        "99:59:59",
        "25:00:00",
        ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],
    )
)

def get_max(nums: str):
    res = ""
    cnt = 0
    for num in nums:
        if num == "K":
            temp = (10 ** cnt) * 5
            res += str(temp)
            cnt = 0
        else:
            cnt += 1

    if cnt:
        res += "1" * cnt

    return res


def get_min(nums: str):
    res = ""
    cnt = 0

    for num in nums:
        if num == "K":
            if cnt:
                res += "1" + ("0" * (cnt - 1)) + "5"
                cnt = 0
            else:
                res += "5"
        else:
            cnt += 1

    if cnt:
        res += "1" + ("0" * (cnt - 1))

    return res


nums = input()
print(get_max(nums))
print(get_min(nums))
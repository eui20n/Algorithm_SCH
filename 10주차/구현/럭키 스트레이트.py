def check(num):
    mid_num = len(num) // 2

    right_num = num[0: mid_num]
    left_num = num[mid_num: len(num)]

    if sum(right_num) == sum(left_num):
        return "LUCKY"
    return "READY"


if __name__ == "__main__":
    number = list(map(int, input()))
    print(check(number))

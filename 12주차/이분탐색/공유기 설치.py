def binary_search(start, end):
    while True:
        if start >= end:
            break

        mid = (start + end) // 2
        check = check_iptime(mid)

        if check:
            start = mid + 1
        else:
            end = mid

    return end


def check_iptime(num):
    idx = 0
    cnt = 1

    for x in range(1, house_num):
        dist = house[x] - house[idx]
        if dist > num:
            idx = x
            cnt += 1

    if cnt < ip_time:
        return False
    return True


if __name__ == "__main__":
    house_num, ip_time = map(int, input().split())
    house = []
    for _ in range(house_num):
        temp_input = int(input())
        house.append(temp_input)
    house.sort()
    house_set = set(house)

    print(binary_search(0, 1000000000))

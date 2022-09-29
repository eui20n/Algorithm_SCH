def check_num(num):
    temp_num = 0

    for length in lengths:
        temp_num += 0 if num > length else length - num

    return temp_num


def binary_search():
    start = 1
    end = 2000000000

    while True:
        if start >= end:
            return start

        mid = (start + end) // 2
        num = check_num(mid)

        if num > M:
            start = mid + 1

        else:
            end = mid


def main():
    result = binary_search()
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    lengths = list(map(int, input().split()))

    print(main())
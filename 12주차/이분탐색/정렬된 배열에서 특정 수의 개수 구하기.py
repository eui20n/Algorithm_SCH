def lower_bound(start, end, target):
    while True:
        if start >= end:
            return start

        mid = (start + end) // 2

        if num_list[mid] == target:
            end = mid - 1
        elif num_list[mid] > target:
            end = mid - 1
        elif num_list[mid] < target:
            start = mid + 1


def upper_bound(start, end, target):
    while True:
        if start >= end:
            return start

        mid = (start + end) // 2

        if num_list[mid] == target:
            start = mid + 1
        elif num_list[mid] > target:
            end = mid - 1
        elif num_list[mid] < target:
            start = mid + 1


if __name__ == '__main__':
    N, num = map(int, input().split())
    num_list = list(map(int, input().split()))

    upper = upper_bound(0, N, num)
    lower = lower_bound(0, N, num)

    # print(f"upper : {upper}, lower : {lower}")

    result = upper - lower
    print(result if result != 0 else -1)
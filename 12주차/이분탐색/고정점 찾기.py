def binary_search(start, end):
    no_answer = -1

    while True:
        if start >= end:
            break

        mid = (start + end) // 2

        if num_list[mid] == mid:
            return mid
        elif num_list[mid] > mid:
            end = mid - 1
        elif num_list[mid] < mid:
            start = mid + 1

    if num_list[start] == start:
        return start
    return no_answer


if __name__ == '__main__':
    N = int(input())
    num_list = list(map(int, input().split()))
    print(binary_search(0, N))
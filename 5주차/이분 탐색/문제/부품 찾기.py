def binary_search(num):
    start = 0
    end = len(N_part)

    while True:
        if start >= end:
            return "no"

        mid = (start + end) // 2

        if N_part[mid] > num:
            end = mid - 1

        if N_part[mid] < num:
            start = mid + 1

        if N_part[mid] == num:
            return "yes"


def main():
    for m in M_part:
        print(binary_search(m), end=" ")


if __name__ == '__main__':
    N = int(input())
    N_part = list(map(int, input().split()))
    N_part.sort()

    M = int(input())
    M_part = list(map(int, input().split()))

    main()
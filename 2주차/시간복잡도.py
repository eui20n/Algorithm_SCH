import time
import random


def sum_n(n):
    """ n """
    result = 0
    for num in range(n):
        result += num


def n_by_n(n):
    """ n**2 """
    for num_1 in range(n):
        for num_2 in range(n):
            pass
    print(f"{n} x {n} = {n ** 2}")


def binary_search(n):
    """ 이분 탐색으로 O(logn)"""
    start = 1
    end = n
    while True:
        if start >= end:
            break

        mid = (start + end)//2

        if mid > start:
            end = mid - 1
        else:
            start = mid + 1


def main():
    """ 시간 별로 출력해줄 함수 """
    num_n = [10, 100, 1000, 10000, 100000]

    print("logn의 복잡도")
    for n in num_n:
        start_time = time.time()
        binary_search(n)
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")

    print("n의 시간 복잡도")
    for n in num_n:
        start_time = time.time()
        sum_n(n)
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")

    print("nlogn의 복잡도")
    for n in num_n:
        arr = [x for x in range(n)]
        random.shuffle(arr)
        start_time = time.time()
        arr.sort()
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")

    print("n^2의 시간 복잡도")
    for n in num_n:
        start_time = time.time()
        n_by_n(n)
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")


if __name__ == "__main__":
    main()

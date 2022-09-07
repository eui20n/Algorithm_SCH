import time


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


def main():
    """ 시간 별로 출력해줄 함수 """
    num_n = [10, 100, 1000, 10000, 100000]
    print("2번 과제")
    for n in num_n:
        start_time = time.time()
        sum_n(n)
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")

    print("3번 과제")
    for n in num_n:
        start_time = time.time()
        n_by_n(n)
        end_time = time.time()
        print(f"{n} time : {round(end_time - start_time, 2)}")


if __name__ == "__main__":
    main()
from random_list import make_random_list


def quick_sort():
    pass


if __name__ == '__main__':
    test_list = make_random_list(10)
    print(f"정렬 전 : {test_list}")

    sorted_arr = quick_sort()
    print(f"정렬 후 : {sorted_arr}")

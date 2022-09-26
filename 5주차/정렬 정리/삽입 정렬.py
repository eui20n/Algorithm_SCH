import random_list


def insertion_sort():
    length = len(test_list)

    for x in range(1, length):
        for y in range(x, 0, -1):
            num = test_list[y]
            next_num = test_list[y - 1]

            if num > next_num:
                break

            test_list[y], test_list[y - 1] = test_list[y - 1], test_list[y]

    return test_list


if __name__ == '__main__':
    test_list = random_list.make_random_list(10)
    print(f"정렬 전 : {test_list}")

    sorted_arr = insertion_sort()
    print(f"정렬 후 : {sorted_arr}")
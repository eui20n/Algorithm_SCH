import random_list


def selection_sort():
    """ 선택 정렬 """
    length = len(test_list)

    for x in range(length):
        min_num = test_list[x]
        min_idx = x
        for y in range(x, length):
            next_num = test_list[y]
            next_idx = y

            if min_num > next_num:
                min_num = next_num
                min_idx = next_idx

        if min_idx != x:
            test_list[x], test_list[min_idx] = test_list[min_idx], test_list[x]

    return test_list


if __name__ == '__main__':
    test_list = random_list.make_random_list(10)
    print(f"정렬 전 : {test_list}")

    sorted_arr = selection_sort()
    print(f"정렬 후 : {sorted_arr}")
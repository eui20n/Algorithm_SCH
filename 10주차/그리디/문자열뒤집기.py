def string_reverse(arr):
    part_num = arr[0]

    part_of_zero = 1 if part_num == 0 else 0
    part_of_one = 1 if part_num == 1 else 0

    for idx in arr:
        if idx != part_num:
            part_num = idx

            part_of_zero += 1 if idx == 0 else 0
            part_of_one += 1 if idx == 1 else 0

    return min(part_of_one, part_of_zero)


if __name__ == '__main__':
    num_arr = list(map(int, input()))
    print(string_reverse(num_arr))

"""
[input]
0001100

[output]
1
"""

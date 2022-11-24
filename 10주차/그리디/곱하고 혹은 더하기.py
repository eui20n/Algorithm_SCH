def calc(arr):
    result = 0
    for idx in arr:
        sum_num = result + idx
        mul_num = result * idx

        result = max(sum_num, mul_num)

    return result


if __name__ == '__main__':
    num_arr = list(map(int, input()))

    print(calc(num_arr))

"""
[input-1]
02984
[output-1]
576

[input-2]
567
[output-2]
210

"""

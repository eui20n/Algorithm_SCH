from copy import deepcopy


def put_operator(arr, arr_idx, final_operator):
    if arr_idx == N - 1:
        final_num = compute(final_operator)
        temp.append(final_num)
        return

    temp_operators = deepcopy(arr)

    for operator_idx in range(4):
        operator = temp_operators[operator_idx]
        if operator > 0:
            temp_operators[operator_idx] -= 1
            final_operator.append(operator_idx)
            put_operator(temp_operators, arr_idx + 1, final_operator)
            temp_operators[operator_idx] += 1
            final_operator.pop()


def compute(final_operator):
    result = num_arr[0]

    for idx in range(len(final_operator)):
        operator = final_operator[idx]

        # 더하기
        if operator == 0:
            result += num_arr[idx + 1]
        # 빼기
        if operator == 1:
            result -= num_arr[idx + 1]
        # 곱하기
        if operator == 2:
            result *= num_arr[idx + 1]
        # 나누기
        if operator == 3:
            result = int(result / num_arr[idx + 1])

    return result


if __name__ == '__main__':
    N = int(input())
    num_arr = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    temp = []
    put_operator(operators, 0, [])
    temp.sort()
    print(temp[len(temp) - 1])
    print(temp[0])


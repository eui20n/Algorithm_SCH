def dp():
    dp_table = [0] * (N + 1)
    dp_table[1] = 1
    dp_table[2] = 3

    for idx in range(3, N + 1):
        dp_table[idx] = 2 * dp_table[idx - 2] + dp_table[idx - 1]

    return dp_table[N]


if __name__ == '__main__':
    N = int(input())
    print(dp())

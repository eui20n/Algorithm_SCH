def dp(num):
    dp_table = [0] * (num + 1)

    dp_table[1] = 0

    for idx in range(2, num + 1):
        if idx % 2 == 0:
            dp_table[idx] = min(dp_table[idx // 2], dp_table[idx - 1]) + 1
            continue

        if idx % 3 == 0:
            dp_table[idx] = min(dp_table[idx // 3], dp_table[idx - 1]) + 1
            continue

        if idx % 5 == 0:
            dp_table[idx] = min(dp_table[idx // 5], dp_table[idx - 1]) + 1
            continue

        dp_table[idx] = dp_table[idx - 1] + 1

    return dp_table[num]


if __name__ == '__main__':
    N = int(input())
    print(dp(N))
def dp():
    dp_table = [0 for _ in range(N)]
    dp_table[0] = 1
    idx_2 = idx_3 = idx_5 = 0
    next_2, next_3, next_5 = 2, 3, 5

    for x in range(1, N):
        dp_table[x] = min(next_2, next_3, next_5)
        if dp_table[x] == next_2:
            idx_2 += 1
            next_2 = dp_table[idx_2] * 2
        if dp_table[x] == next_3:
            idx_3 += 1
            next_3 = dp_table[idx_3] * 2
        if dp_table[x] == next_5:
            idx_5 += 1
            next_5 = dp_table[idx_5] * 2

    return dp_table[N - 1]


if __name__ == "__main__":
    N = int(input())
    print(dp())

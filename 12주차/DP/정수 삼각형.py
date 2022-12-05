def dp():
    dp_table = [[0 for _ in range(501)] for _ in range(N + 1)]

    if len(T) <= 1:
        dp_table[1][0] = T[0][0]
    else:
        dp_table[1][0] = T[0][0]
        dp_table[2][0] = T[0][0] + T[1][0]
        dp_table[2][1] = T[0][0] + T[1][1]

    for x in range(3, N + 1):
        for y in range(1, len(T[x - 1])):
            dp_table[x][0] = dp_table[x - 1][0] + T[x - 1][0]
            dp_table[x][y] = max(dp_table[x - 1][y - 1] + T[x - 1][y], dp_table[x - 1][y] + T[x - 1][y])

    return max(dp_table[N])


if __name__ == "__main__":
    N = int(input())
    T = [list(map(int, input().split())) for _ in range(N)]

    print(dp())

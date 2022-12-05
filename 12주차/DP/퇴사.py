def dp():
    dp_table = [0 for _ in range(25)]

    for idx in range(N):
        if dp_table[idx] > dp_table[idx + 1]:
            dp_table[idx + 1] = dp_table[idx]
        if dp_table[idx + T[idx]] < dp_table[idx] + P[idx]:
            dp_table[idx + T[idx]] = dp_table[idx] + P[idx]

    return dp_table[N]


if __name__ == "__main__":
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)

    print(dp())
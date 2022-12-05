def dp():
    dp_table = [1 for _ in range(N + 1)]

    for x in range(1, len(dp_table)):
        for y in range(x, 0, -1):
            if num[x - 1] <= num[y - 1]:
                continue
            else:
                dp_table[x] = max(dp_table[x], dp_table[y] + 1)

    return N - max(dp_table)


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    num.reverse()

    print(dp())

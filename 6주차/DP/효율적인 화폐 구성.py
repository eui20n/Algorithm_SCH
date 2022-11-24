def dp():
    Inf = float('inf')

    dp_table = [Inf for _ in range(M + 1)]

    start_num = min(dollars)

    for idx in dollars:
        dp_table[idx] = 1

    for idx in range(start_num, M + 1):
        for dollar in dollars:
            dp_table[idx] = min(dp_table[idx - dollar] + 1, dp_table[idx])

    result = dp_table[M] if dp_table[M] != Inf else -1

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    dollars = []
    for _ in range(N):
        temp = int(input())
        dollars += [temp]

    if max(dollars) > M:
        print(-1)
    else:
        print(dp())
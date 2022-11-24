def dp():
    # 전에 창고를 공격한 경우, 전의 창고를 공격하지 않은 경우
    dp_table = [[0, 0] for _ in range(N + 1)]
    dp_table[1][1] = arr[1]

    for idx in range(2, N + 1):
        dp_table[idx][0] = dp_table[idx - 1][1]
        dp_table[idx][1] = max(dp_table[idx - 1][0] + arr[idx], dp_table[idx - 1][1])

    return max(dp_table[N])


if __name__ == '__main__':
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(dp())

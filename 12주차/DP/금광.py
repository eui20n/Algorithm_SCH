def gold_mine(n, m, data):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        dp[x][0] = data[x][0]

    for y in range(1, m):
        for x in range(n):
            if x + 1 < n:
                temp = data[x][y] + dp[x + 1][y - 1]
                dp[x][y] = max(dp[x][y], temp)

            elif x - 1 >= 0:
                temp = data[x][y] + dp[x - 1][y - 1]
                dp[x][y] = max(dp[x][y], temp)

            temp = data[x][y] + dp[x][y - 1]
            dp[x][y] = max(dp[x][y], temp)
    max_list = []

    for x in range(n):
        max_list.append(max(dp[x]))

    print(max(max_list))


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        temp = list(map(int, input().split()))

        data = []

        for k in range(0, len(temp), 4):
            data.append(temp[k: k + 4])

        gold_mine(n, m, data)

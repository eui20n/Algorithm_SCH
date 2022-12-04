def main():
    chicken, home = change_board()
    max_chicken(0, chicken, home)


def max_chicken(start, chicken, home):
    if len(chicken_loc) > M:
        return
    if 0 < len(chicken_loc) <= M:
        result = [float('inf') for _ in range(len(home))]

        for x in chicken_loc:
            for y in range(len(home)):
                if result[y] > abs(x[0] - home[y][0]) + abs(x[1] - home[y][1]) and result[y] != 0:
                    result[y] = abs(x[0] - home[y][0]) + abs(x[1] - home[y][1])

        if num[0] > sum(result):
            num[0] = sum(result)

    for x in range(start, len(chicken)):
        if chicken[x] not in chicken_loc:
            chicken_loc.append(chicken[x])
            max_chicken(start + 1, chicken, home)
            chicken_loc.pop()


def change_board():
    chicken = []
    home = []

    for x in range(N):
        for y in range(N):
            if board[x][y] == 2:
                chicken.append([x, y])
                board[x][y] = 0
            elif board[x][y] == 1:
                home.append([x, y])

    return chicken, home


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chicken_loc = []
    num = [float('inf')]
    main()
    print(num[0])

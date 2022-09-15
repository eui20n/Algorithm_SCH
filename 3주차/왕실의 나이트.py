def knight():
    """ 왕실의 나이트 """
    loc = input()
    col_loc = ["a", "b", "c", "d", "e", "f", "g"]

    x, y = [int(loc[1]) - 1, col_loc.index(loc[0])]

    dx = [-2, 2, -2, 2, 1, 1, -1, -1]
    dy = [1, 1, -1, -1, -2, 2, -2, 2]

    cnt = 0

    for z in range(8):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= 8:
            continue
        if 0 > ny or ny >= 8:
            continue

        cnt += 1

    print(cnt)


if __name__ == "__main__":
    knight()

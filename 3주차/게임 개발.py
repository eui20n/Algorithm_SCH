def game():
    """ 게임 개발 함수 """
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = [3, 0, 1, 2]

    x, y, d = start_x, start_y, start_d

    cnt = 1
    end_con = 0

    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[start_x][start_y] = True

    while True:
        if end_con == 4:
            break

        d = 0 if d >= 4 else d + 1

        nx = x + dx[direction[d]]
        ny = y + dy[direction[d]]

        if 0 > nx or nx >= R:
            end_con += 1
            continue
        if 0 > ny or ny >= C:
            end_con += 1
            continue
        if board[nx][ny] == 1:
            end_con += 1
            continue

        x = nx
        y = ny
        cnt += 1
        end_con = 0

    print(cnt)


if __name__ == "__main__":
    R, C = map(int, input().split())
    start_x, start_y, start_d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    game()


# 0 : 북쪽
# 1 : 동쪽
# 2 : 남족
# 3 : 서쪽
# 왼쪽으로 돔
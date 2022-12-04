def back_tracking(cnt):
    global result

    if cnt == 3:
        if check():
            result = True
            return

    else:
        for x in range(N):
            for y in range(N):
                if board[x][y] == "X":
                    board[x][y] = "O"
                    back_tracking(cnt + 1)
                    board[x][y] = "X"


def check():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for teacher in teachers:
        for z in range(4):
            nx, ny = teacher

            while True:
                if 0 > nx or nx >= N:
                    break
                if 0 > ny or ny >= N:
                    break
                if board[nx][ny] == "O":
                    break
                if board[nx][ny] == "S":
                    return False

                nx += dx[z]
                ny += dy[z]

    return True


if __name__ == "__main__":
    N = int(input())
    board = []
    teachers = []

    for x in range(N):
        input_value = list(input().split())
        board.append(input_value)
        for y in range(N):
            if board[x][y] == "T":
                teachers.append([x, y])

    result = False

    back_tracking(0)

    print("YES" if result else "NO")

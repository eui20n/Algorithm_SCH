def solution(key, lock):
    M = len(key)
    N = len(lock)
    board_size = M * 2 + N

    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    board = board_center(lock, board, M, N)

    for _ in range(4):
        key = rotate_arr(key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                attach(x, y, N, key, board)
                if check(board, M, N):
                    return True
                detach(x, y, N, key, board)


def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True


def board_center(arr_lock, arr_board, M, N):
    for x in range(N):
        for y in range(N):
            arr_board[M + x][M + y] = arr_lock[x][y]
    return arr_board


def rotate_arr(arr):
    temp = []
    for x in arr:
        temp.append(reversed(x))

    zip_list = list(zip(*temp))

    for x in range(len(zip_list)):
        temp[x] = list(zip_list[x])

    return temp


def show_arr(arr):
    print(*arr, sep="\n")
    print()


if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))

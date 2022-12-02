from collections import deque


def check_start():
    temp = []

    for x in range(N):
        for y in range(N):
            idx = board[x][y]
            if idx != 0:
                temp.append([x, y, idx])

    temp.sort(key=lambda x: x[2])

    return temp


def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append(start)

    time = 0

    while q:
        if time == S:
            return

        p = q.popleft()
        temp = deque()

        for x, y, virus in p:
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]
                if 0 > nx or nx >= N:
                    continue
                if 0 > ny or ny >= N:
                    continue
                if board[nx][ny] == 0:
                    board[nx][ny] = virus
                    temp.append([nx, ny, virus])

        q.append(temp)
        time += 1


def main():
    start_point = check_start()
    bfs(start_point)


if __name__ == "__main__":
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    main()
    print(board[X - 1][Y - 1])

from collections import deque


def bfs(r, c, arr, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[0][0] = True

    q = deque()
    q.append([0, 0, 1])

    while q:
        x, y, cnt = q.popleft()
        if x == r - 1 and y == c - 1:
            return cnt

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= r:
                continue
            if 0 > ny or ny >= c:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == 0:
                continue

            q.append([nx, ny, cnt + 1])


def main():
    R, C = map(int, input().split())
    board = [list(map(int, input())) for _ in range(R)]

    visited = [[False for _ in range(C)] for _ in range(R)]

    return bfs(R, C, board, visited)


if __name__ == "__main__":
    print(main())


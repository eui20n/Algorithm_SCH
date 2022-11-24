def visited_init(r, c, arr):
    visited = [[False for _ in range(c)] for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if arr[x][y] == 1:
                visited[x][y] = True

    return visited


# def dfs(r, c, arr, x, y, visited):
#     if arr[x][y] == 1:
#         return
#
#     visited[x][y] = True
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     for z in range(4):
#         nx = x + dx[z]
#         ny = y + dy[z]
#         if 0 > nx or nx >= r:
#             continue
#         if 0 > ny or ny >= c:
#             continue
#         if visited[nx][ny]:
#             continue
#
#         dfs(r, c, arr, nx, ny, visited)


def dfs(r, c, arr, x, y, visited):
    if 0 > x or x >= r:
        return
    if 0 > y or y >= c:
        return
    if arr[x][y] == 1:
        return
    if visited[x][y]:
        return

    visited[x][y] = True

    dfs(r, c, arr, x + 1, y, visited)
    dfs(r, c, arr, x - 1, y, visited)
    dfs(r, c, arr, x, y + 1, visited)
    dfs(r, c, arr, x, y - 1, visited)


def main():
    R, C = map(int, input().split())
    board = [list(map(int, input())) for _ in range(R)]

    visited = visited_init(R, C, board)
    result = 0

    for x in range(R):
        for y in range(C):
            if not visited[x][y]:
                dfs(R, C, board, x, y, visited)
                result += 1

    return result


if __name__ == "__main__":
    print(main())

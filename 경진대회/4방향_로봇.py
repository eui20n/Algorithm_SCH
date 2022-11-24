def cnt_move(arr):
    direction = {"W": (0, 1), "E": (0, -1), "S": (1, 0), "N": (-1, 0)}

    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[0][0] = 1
    ans = 0

    x, y = 0, 0
    for next_dir in arr:
        nx = x + direction[next_dir][0]
        ny = y + direction[next_dir][1]
        if 0 > nx or nx >= R:
            visited[x][y] += 1
            ans = max(ans, visited[x][y])
            continue
        if 0 > ny or ny >= C:
            visited[x][y] += 1
            ans = max(ans, visited[x][y])
            continue

        visited[nx][ny] += 1
        ans = max(ans, visited[nx][ny])
        x = nx
        y = ny

    return ans


if __name__ == '__main__':
    R, C, cnt = map(int, input().split())
    move_command = list(input())
    result = cnt_move(move_command)
    print(result)

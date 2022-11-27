from collections import deque


def check_state(arr):
    start_point = []
    change_wall = []

    for x in range(R):
        for y in range(C):
            if arr[x][y] == 2:
                start_point.append([x, y])
            elif arr[x][y] == 0:
                change_wall.append([x, y])

    return start_point, change_wall


def check_lab(arr, start, change):

    result = -1

    for x in range(len(change)):
        for y in range(x + 1, len(change)):
            for z in range(y + 1, len(change)):
                x_r, x_c = change[x]
                y_r, y_c = change[y]
                z_r, z_c = change[z]

                arr[x_r][x_c] = 1
                arr[y_r][y_c] = 1
                arr[z_r][z_c] = 1
                result = max(result, bfs(arr, start))

                arr[x_r][x_c] = 0
                arr[y_r][y_c] = 0
                arr[z_r][z_c] = 0

    return result


def bfs(arr, start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    new_wall = [x[:] for x in arr]

    q = deque()
    q.append(start)

    while q:
        p = q.popleft()
        for x, y in p:
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]
                if 0 > nx or nx >= R:
                    continue
                if 0 > ny or ny >= C:
                    continue
                if new_wall[nx][ny] == 1:
                    continue
                if new_wall[nx][ny] == 2:
                    continue

                q.append([[nx, ny]])
                new_wall[nx][ny] = 2

    return check_safe_zone(new_wall)


def check_safe_zone(arr):
    cnt = 0
    for x in range(R):
        for y in range(C):
            if arr[x][y] == 0:
                cnt += 1

    return cnt


def main(arr):
    start_point, change_wall = check_state(arr)
    print(check_lab(arr, start_point, change_wall))


if __name__ == "__main__":
    R, C = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(R)]
    main(lab)

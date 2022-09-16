

def visited_init():
    """ 방문 처리 리스트를 만드는 함수 """
    visited = [[False for _ in range(C)] for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if board[x][y]:
                visited[x][y] = True

    return visited



def game():
    """ 게임 개발 함수 """
    # 서 남 동 북 서 남 동 북
    dx = [0, 1, 0, -1, 0, 1, 0, -1]
    dy = [-1, 0, 1, 0, -1, 0, 1, 0]

    x, y, d = start_x, start_y, start_d

    visited = visited_init()
    visited[x][y] = True

    cnt = 1

    while True:
        go_back = True

        for z in range(d, d + 4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                continue

            x = nx
            y = ny
            cnt += 1
            d = z - 4 if z >= 4 else z
            visited[nx][ny] = True
            go_back = False
            break

        if go_back:
            nx = x - dx[d]
            ny = y - dy[d]

            if board[nx][ny] == 1:
                return cnt

            x = nx
            y = ny


if __name__ == "__main__":
    R, C = map(int, input().split())
    start_x, start_y, start_d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    print(game())

def visited_init():
    """ 방문 처리 리스트를 만드는 함수 """
    visited = [[False for _ in range(C)] for _ in range(R)]

    """
        바다인 부분으로 가면 안됨, 즉 바다는 이미 방문 처리가 되어있어야함
        그래서 바다인 부분을 True로 바꿔줌
    """
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                visited[x][y] = True

    return visited


def game():
    """ 게임 개발 함수 """

    """
        서 남 동 북 서 남 동 북
        이렇게 뒤에다가 하나 더 붙인 이유는 계산의 편의를 위해서
        만약 [서 남 동 북] 이라고 가정을 하면 초기 방향이 1이면 시계 반대 방향으로 돌면 결국 4가 나오는데, 이 때 이 수를 0으로 만들어줘야함
        근데 이렇게 하면 이러한 과정이 사라짐
    """
    dx = [0, 1, 0, -1, 0, 1, 0, -1]
    dy = [-1, 0, 1, 0, -1, 0, 1, 0]

    x, y, d = start_x, start_y, start_d

    """
        방문 처리 리스트를 만들고 처음의 값은 이미 방문을 했기 때문에 True로 해줌
    """
    visited = visited_init()
    visited[x][y] = True

    cnt = 1

    while True:
        # 후진을 해야하는지 알려주는 변수
        go_back = True

        """
            현재 방향에서 시계 반대 방향으로 4방향을 봄
            이 과정에서 갈 수 있는 곳이 나오면 가고 for문을 종료 시켜서 while문을 다시 돌림
            근데 그냥 for문을 종료 시키면 아래의 식이 수행이 되기 때문에 go_back = False로 해줌
        """
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
            # 만약에 d의 값이 4가 넘으면 다시 4를 빼줌 -> 이렇게 해야지 8방향으로 보는게 유지가 됨
            d = z - 4 if z >= 4 else z
            visited[nx][ny] = True
            go_back = False
            break

        """
            위에서 갈 곳이 없어서 후진을 해야하는 경우
            후진이라는 것은 현재 방향의 반대 방향, 즉 방향을 더해주는게 아니라 빼주면 됨
            이렇게 후진을 한게 바다이면 종료
            아니면 후진한 값을 넘겨주고 while문 반복
        """
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

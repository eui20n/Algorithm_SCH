def up_down_left_right():
    """ 상하좌우 함수 """
    N = int(input())
    direction = list(map(str, input().split()))
    dx = []
    dy = []
    for d in direction:
        if d == "U":
            dx.append(-1)
            dy.append(0)
            continue
        if d == "D":
            dx.append(1)
            dy.append(0)
            continue
        if d == "L":
            dx.append(0)
            dy.append(-1)
            continue
        if d == "R":
            dx.append(0)
            dy.append(1)
            continue

    x = 1
    y = 1

    for d in range(len(direction)):
        nx = x + dx[d]
        ny = y + dy[d]
        if 1 > nx or nx >= N + 1:
            continue
        if 1 > ny or ny >= N + 1:
            continue
        x = nx
        y = ny

    print(x, y)


if __name__ == "__main__":
    up_down_left_right()
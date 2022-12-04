from collections import deque


def Dummy():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    snake_idx = 0
    snake_time = snake[snake_idx][0]
    snake_dir = snake[snake_idx][1]
    eat_apple = set([])

    time = 0
    dir = 0

    body = deque()
    body.append([0, 0])

    while True:
        time += 1
        eat_apple_check = False

        head_x = body[0][0]
        head_y = body[0][1]
        new_head_x = head_x + dx[dir]
        new_head_y = head_y + dy[dir]

        body.appendleft([new_head_x, new_head_y])
        if 0 > new_head_x or new_head_x >= N:
            return time
        if 0 > new_head_y or new_head_y >= N:
            return time

        for x in range(1, len(body)):
            if new_head_x == body[x][0] and new_head_y == body[x][1]:
                return time

        for idx in range(len(apple)):
            apple_x = apple[idx][0]
            apple_y = apple[idx][1]

            if idx in eat_apple:
                continue
            elif apple_x != new_head_x:
                continue
            elif apple_y != new_head_y:
                continue
            eat_apple.add(idx)
            eat_apple_check = True

        if not eat_apple_check:
            body.pop()

        if time == snake_time:
            if snake_dir == "D":
                dir += 1
                if dir > 3:
                    dir = 0
            else:
                dir -= 1
                if dir < 0:
                    dir = 3

            snake_idx = snake_idx if snake_idx + 1 >= snake_cnt else snake_idx + 1
            snake_time = snake[snake_idx][0]
            snake_dir = snake[snake_idx][1]


if __name__ == "__main__":
    N = int(input())
    apple_cnt = int(input())
    apple = []
    for _ in range(apple_cnt):
        apple_r, apple_c = map(int, input().split())
        apple.append([apple_r - 1, apple_c - 1])
    snake_cnt = int(input())
    snake = []
    for _ in range(snake_cnt):
        snake_time, snake_dir = list(input().split())
        snake.append([int(snake_time), snake_dir])

    print(Dummy())

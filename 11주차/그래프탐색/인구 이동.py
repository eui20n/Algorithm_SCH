from collections import deque


def population_move(visited, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[y] |= 1 << x

    q = deque()
    q.append([x, y])

    group = [[x, y]]
    sum_num = population[x][y]

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= N:
                continue
            if visited[ny] & (1 << nx):
                continue

            country_1 = population[x][y]
            country_2 = population[nx][ny]
            change_value = abs(country_1 - country_2)

            if L <= change_value <= R:
                group.append([nx, ny])
                q.append([nx, ny])
                visited[ny] |= 1 << nx
                sum_num += country_2

    return group, sum_num


def change(arr, change_value):
    for x, y in arr:
        population[x][y] = change_value


def main():
    result = 0

    while True:
        visited = [0 for _ in range(N)]
        cnt = 1

        for x in range(N):
            for y in range(N):
                if not (visited[y] & (1 << x)):
                    change_population, sum_num = population_move(visited, x, y)
                    length = len(change_population)
                    change_value = sum_num // length
                    change(change_population, change_value)
                    cnt = max(length, cnt)

        if cnt == 1:
            return result
        result += 1


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(N)]
    print(main())

def floyd_warshall():
    result = 0
    cnt = 0

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                graph[y][z] = min(graph[y][z], graph[y][x] + graph[x][z])

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if (graph[x][y] != 0 and graph[x][y] != INF) or (graph[y][x] != 0 and graph[y][x] != INF):
                cnt += 1

        if cnt == N - 1:
            result += 1
        cnt = 0

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    INF = float('inf')
    graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(N):
        idx_1, idx_2 = map(int, input().split())
        graph[idx_1][idx_2] = 1

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if x == y:
                graph[x][y] = 0

    print(floyd_warshall())

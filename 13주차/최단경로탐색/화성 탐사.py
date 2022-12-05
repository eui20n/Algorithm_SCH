import heapq


def dijkstra():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[INF for _ in range(N)] for _ in range(N)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    dist[x][y] = graph[x][y]

    while q:
        pop_dist, x, y = heapq.heappop(q)
        if dist[x][y] < pop_dist:
            continue
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= N:
                continue
            cost = pop_dist + graph[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    return dist[N - 1][N - 1]


if __name__ == "__main__":
    T = int(input())
    INF = float('inf')
    for _ in range(T):
        N = int(input())
        graph = [list(map(int, input().split())) for _ in range(N)]
        print(dijkstra())

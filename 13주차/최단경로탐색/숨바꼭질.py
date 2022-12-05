import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        dist_2, now = heapq.heappop(q)
        if dist[now] < dist_2:
            continue
        for x in graph[now]:
            cost = dist_2 + x[1]
            if cost < dist[x[0]]:
                dist[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


def main():
    dijkstra(start)

    max_node = 0
    max_distance = 0
    result = []

    for idx in range(1, n + 1):
        if max_distance < dist[idx]:
            max_node = idx
            max_distance = dist[idx]
            result = [max_node]
        elif max_distance == dist[idx]:
            result.append(idx)

    print(max_node, max_distance, len(result))


if __name__ == "__main__":
    n, m = map(int, input().split())
    INF = float('inf')

    start = 1
    graph = [[] for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append([b, 1])
        graph[b].append([a, 1])

    main()
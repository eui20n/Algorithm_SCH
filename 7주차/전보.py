import heapq


def dijkstra(start):
    """ 다익스트라 """
    Inf = -float('inf')
    visited = [Inf for _ in range(N + 1)]
    visited[start] = 0

    heap = []
    for city, cost in connected_info[start]:
        visited[city] = cost
        heapq.heappush(heap, (city, cost))

    while heap:
        city, cost = heapq.heappop(heap)

        for next_city, next_cost in connected_info[city]:
            if visited[city] > visited[next_city]:
                visited[next_city] = visited[city] + next_cost
                heapq.heappush(heap, (next_city, next_cost))

    cnt, max_num = 0, 0

    for num in visited:
        if num == Inf:
            continue
        if num == 0:
            continue

        cnt += 1
        max_num = max(max_num, num)

    return cnt, max_num


if __name__ == '__main__':
    N, M, C = map(int, input().split())
    connected_info = [[] for _ in range(N + 1)]
    for _ in range(M):
        temp_city, other_city, message_time = map(int, input().split())
        connected_info[temp_city].append((other_city, message_time))

    result = dijkstra(C)
    print(*result)

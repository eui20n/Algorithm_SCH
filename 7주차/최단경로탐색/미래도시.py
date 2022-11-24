import heapq


def dijkstra(start, end):
    """ 다익스트라 """

    Inf = float('inf')
    visited = [Inf for _ in range(N + 1)]
    visited[start] = 0

    heap = []
    for item in connected_info[start]:
        visited[item] = 1
        heapq.heappush(heap, item)

    while heap:
        current_heap = heapq.heappop(heap)
        for next_heap in connected_info[current_heap]:
            if visited[current_heap] < visited[next_heap]:
                visited[next_heap] = visited[current_heap] + 1
                heapq.heappush(heap, next_heap)

    return visited[end]


if __name__ == '__main__':
    N, M = map(int, input().split())
    connected_info = [[] for _ in range(N + 1)]
    for _ in range(M):
        company_1, company_2 = map(int, input().split())
        connected_info[company_1].append(company_2)
        connected_info[company_2].append(company_1)

    end_company, middle_company = map(int, input().split())

    result = dijkstra(1, middle_company)
    result += dijkstra(middle_company, end_company)

    print(result if result != float('inf') else -1)

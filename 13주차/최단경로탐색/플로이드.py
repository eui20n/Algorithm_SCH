def floyd_warshall():
    Inf = float("inf")
    all_cost = [[Inf for _ in range(N)] for _ in range(N)]

    for start, end, cost in bus:
        all_cost[start][end] = min(cost, all_cost[start][end])

    for via_idx in range(N):
        for r_idx in range(N):
            for c_idx in range(N):
                if r_idx == c_idx:
                    all_cost[r_idx][c_idx] = 0
                    continue
                if all_cost[r_idx][via_idx] + all_cost[via_idx][c_idx] < all_cost[r_idx][c_idx]:
                    all_cost[r_idx][c_idx] = all_cost[r_idx][via_idx] + all_cost[via_idx][c_idx]

    for r in range(N):
        for c in range(N):
            if all_cost[r][c] == Inf:
                all_cost[r][c] = 0

    return all_cost


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    bus = []
    for _ in range(M):
        start_bus, arrive_bus, bus_cost = map(int, input().split())
        bus.append([start_bus - 1, arrive_bus - 1, bus_cost])
    result_arr = floyd_warshall()

    for result in result_arr:
        print(*result)

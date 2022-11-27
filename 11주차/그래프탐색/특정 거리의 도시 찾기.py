from collections import deque


def find_city(start, end_num):
    visited = [-1 for _ in range(N + 1)]
    visited[start] = 0

    q = deque()
    q.append(start)

    result = []

    while q:
        x = q.popleft()
        for nx in city[x]:
            if visited[nx] != -1:
                continue

            visited[nx] = visited[x] + 1
            q.append(nx)

            if visited[nx] == end_num:
                result.append(nx)

    if len(result) == 0:
        return [-1]
    return result


if __name__ == '__main__':
    N, M, K, X = map(int, input().split())
    city = [[] for _ in range(N + 1)]
    for _ in range(M):
        city_1, city_2 = map(int, input().split())
        city[city_1].append(city_2)

    result = find_city(X, K)
    result.sort()
    print(*result, sep="\n")
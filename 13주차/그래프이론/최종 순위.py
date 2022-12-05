from collections import deque


def topology_sort():
    result = []
    q = deque()

    for x in range(1, n + 1):
        if indegree[x] == 0:
            q.append(x)

    certain = True
    cycle = False

    for x in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for y in range(1, n + 1):
            if graph[now][y]:
                indegree[y] -= 1

                if indegree[y] == 0:
                    q.append(y)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(*result)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        indegree = [0 for _ in range(n + 1)]
        graph = [[False for _ in range(n + 1)] for i in range(n + 1)]

        data = list(map(int, input().split()))

        for x in range(n):
            for y in range(x + 1, n):
                idx_x = data[x]
                idx_y = data[y]

                graph[idx_x][idx_y] = True
                indegree[idx_y] += 1

        m = int(input())
        for x in range(m):
            a, b = map(int, input().split())
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[a] += 1
                indegree[b] -= 1
            else:
                graph[a][b] = True
                graph[b][a] = False
                indegree[a] -= 1
                indegree[b] += 1

        topology_sort()
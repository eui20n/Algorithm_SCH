from collections import deque


def zero_one_bfs(start, end):
    """ 0 - 1 bfs """
    Inf = float('inf')
    visited = [Inf for _ in range(N + 1)]
    visited[start] = 0

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for nx in connected_info[x]:
            if visited[nx] != Inf:
                continue

            # 해당 문제는 모든 가중치가 1이기 때문에 0인 경우는 생각안해됨
            # 가중치가 0인 것이 있다면 이는 appendleft로 앞에 넣으면 됨
            visited[nx] = visited[x] + 1
            q.append(nx)

    return visited[end]


if __name__ == '__main__':
    N, M = map(int, input().split())
    connected_info = [[] for _ in range(N + 1)]
    for _ in range(M):
        company_1, company_2 = map(int, input().split())
        connected_info[company_1].append(company_2)
        connected_info[company_2].append(company_1)

    end_company, middle_company = map(int, input().split())

    result = zero_one_bfs(1, middle_company)
    result += zero_one_bfs(middle_company, end_company)

    print(result if result != float('inf') else -1)

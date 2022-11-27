def find(parent, node):
    if parent[node] == node:
        return node
    p = find(parent, parent[node])
    parent[node] = p
    return p


def union(parent, node_1, node_2):
    node_1 = find(parent, node_1)
    node_2 = find(parent, node_2)

    if node_1 > node_2:
        parent[node_1] = node_2
    else:
        parent[node_2] = node_1


def main():
    node_info = change_input(board)
    parent = [x for x in range(N + 1)]

    for node_1, node_2 in node_info:
        union(parent, node_1, node_2)

    result = parent[trip[0]]

    for idx in trip:
        if result != parent[idx]:
            return "NO"
    return "YES"


def change_input(arr):
    result = []
    for r in range(N):
        for c in range(r, N):
            if arr[r][c] == 1:
                result.append([r + 1, c + 1])
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    trip = list(map(int, input().split()))
    print(main())
    # print(*board, sep="\n")
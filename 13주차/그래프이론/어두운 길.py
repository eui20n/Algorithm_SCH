def find(node):
    if parent[node] == node: return node
    p = find(parent[node])
    parent[node] = p
    return p


def union(node_1, node_2):
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        parent[node_1] = node_2
    else:
        parent[node_2] = node_1


def MST():
    sum_num = 0
    result = 0

    for cost, a, b in edges:
        sum_num += cost

        if find(a) != find(b):
            union(a, b)
            result += cost

    return sum_num - result


if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [x for x in range(N + 1)]
    edges = []

    for _ in range(M):
        x, y, z = map(int, input().split())
        edges.append([z, x, y])
    edges.sort()

    print(MST())

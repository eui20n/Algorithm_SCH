def sort_idx(arr, idx):
    temp = sorted(arr, key=lambda x: x[idx])

    return_arr = []

    for loc in range(len(temp) - 1):
        x = temp[loc][idx]
        nx = temp[loc + 1][idx]
        x_idx = temp[loc][3]
        nx_idx = temp[loc + 1][3]

        return_arr.append([x_idx, nx_idx, abs(x - nx)])

    return return_arr


def connect_planet(arr):
    arr.sort(key=lambda x: x[2])
    result = 0

    for node_1, node_2, cost in arr:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            result += cost

    return result


def find(node):
    if connected_planet[node] == node: return node

    p = find(connected_planet[node])
    connected_planet[node] = p
    return p


def union(node_1, node_2):
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        connected_planet[node_1] = node_2
    else:
        connected_planet[node_2] = node_1


def main():
    final_arr = sort_idx(tunnel, 0) + sort_idx(tunnel, 1) + sort_idx(tunnel, 2)
    print(*final_arr, sep="\n")
    result = connect_planet(final_arr)
    return result


if __name__ == "__main__":
    N = int(input())
    tunnel = []
    for idx in range(1, N + 1):
        a, b, c = map(int, input().split())
        tunnel.append([a, b, c, idx])
    connected_planet = [x for x in range(N + 1)]

    print(main())

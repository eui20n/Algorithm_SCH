def find(node):
    if gate_parent[node] == node: return node

    p = find(gate_parent[node])
    gate_parent[node] = p
    return p


def union(node_1, node_2):
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        gate_parent[node_1] = node_2

    else:
        gate_parent[node_2] = node_1


def docking():
    max_docking_num = 0

    for node in plane_info:
        find_node = find(node)

        if find_node == 0:
            return max_docking_num

        max_docking_num += 1
        union(node, find_node - 1)

    return max_docking_num


if __name__ == "__main__":
    G = int(input())
    P = int(input())
    plane_info = []
    for _ in range(P):
        plane_info.append(int(input()))

    gate_parent = [x for x in range(G + 1)]

    print(docking())

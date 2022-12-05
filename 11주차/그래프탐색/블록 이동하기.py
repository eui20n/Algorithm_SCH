from collections import deque


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for x in range(n):
        for y in range(n):
            new_board[x + 1][y + 1] = board[x][y]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


def get_next_pos(pos, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for z in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[z], pos1_y + dy[z], pos2_x + dx[z], pos2_y + dy[z]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:
        for x in [-1, 1]:
            if board[pos1_x + x][pos1_y] == 0 and board[pos2_x + x][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + x, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + x, pos2_y)})
    elif pos1_y == pos2_y:
        for x in [-1, 1]:
            if board[pos1_x][pos1_y + x] == 0 and board[pos2_x][pos2_y + x] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + x)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + x)})
    return next_pos


if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))
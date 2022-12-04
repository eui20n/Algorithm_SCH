def solution(n, build_frame):
    answer = []
    REMOVE = 0
    INSTALL = 1

    for x, y, build, command in build_frame:
        if command == REMOVE:
            answer.remove([x, y, build])
            if not check(answer):
                answer.append([x, y, build])

        elif command == INSTALL:
            answer.append([x, y, build])
            if not check(answer):
                answer.remove([x, y, build])
    answer.sort()
    return answer


def check(arr):
    PILLAR = 0
    PAPER = 1
    print(*arr, sep="\n")
    print()

    for x, y, build in arr:
        if build == PILLAR:
            if y == 0:
                continue
            if [x - 1, y, 1] in arr or [x, y, 1] in arr:
                continue
            if [x, y - 1, 0] in arr:
                continue

        if build == PAPER:
            if [x, y - 1, 0] in arr or [x + 1, y - 1, 0] in arr:
                continue
            if [x - 1, y, 1] in arr and [x + 1, y, 1] in arr:
                continue
        return False
    return True


if __name__ == "__main__":
    n = 5
    build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]
    print(*solution(n, build_frame), sep="\n")

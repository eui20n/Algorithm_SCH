def measurement(direction):
    if direction == "left":
        for c in range(N):
            for r in range(N):
                if injury[r][c] == 1:
                    return c

    elif direction == "right":
        for c in range(N - 1, -1, -1):
            for r in range(N):
                if injury[r][c] == 1:
                    return c

    elif direction == "top":
        for r in range(N):
            for c in range(N):
                if injury[r][c] == 1:
                    return r

    elif direction == "bottom":
        for r in range(N - 1, -1, -1):
            for c in range(N):
                if injury[r][c] == 1:
                    return r


def main():
    left = measurement("left")
    right = measurement("right")
    top = measurement("top")
    bottom = measurement("bottom")

    # print(f"left : {left}, right : {right}, top : {top}, bottom : {bottom}")

    result = (right - left + 1) * (bottom - top + 1)
    return result


if __name__ == '__main__':
    N = int(input())
    injury = [list(map(int, input().split())) for _ in range(N)]

    print(main())

def check_build_house():
    standard_num = min(R, C)
    standard = [x for x in range(1, standard_num + 1)]
    # standard = [x for x in range(standard_num, 0, -1)]
    print(standard)
    result = 0

    for r in range(R):
        for c in range(C):
            if land[r][c] == 0:
                continue

            temp_num = measurement(r, c, standard, result)
            result = max(temp_num, result)

    return result ** 2


def measurement(r, c, arr, max_num):
    for add in arr:
        if add <= max_num:
            continue

        if 0 > r + add or r + add >= R:
            return add - 1
        if 0 > c + add or c + add >= C:
            return add - 1

        for next_r in range(r, r + add):
            for next_c in range(c, c + add):
                if land[next_r][next_c] == 0:
                    return add - 1


if __name__ == '__main__':
    R, C = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(R)]
    print(check_build_house())

# 뒤에서 부터 해서 처음으로 만족하면 끝내면 됨

"""
[input-1]
4 5
0 1 1 0 1 
0 1 1 0 1 
1 0 1 1 0 
1 1 1 1 1 
[output-1]
4
[input-2]
4 5
1 1 1 1 1
1 1 1 0 1
1 1 1 0 1
1 0 0 1 1 
[output-2]
9
"""
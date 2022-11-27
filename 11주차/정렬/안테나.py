def main():
    house.sort()
    length_house = len(house)

    # 짝수
    if length_house % 2 == 0:
        temp = house[length_house // 2 - 1]
        temp_1 = house[length_house // 2]

        result = check_min(temp, temp_1)

    # 홀수
    if length_house % 2 == 1:
        result = house[length_house // 2]

    return result


def check_min(num_1, num_2):
    temp_result_1 = 0
    temp_result_2 = 0

    for idx in range(len(house)):
        temp_result_1 += abs(house[idx] - num_1)
        temp_result_2 += abs(house[idx] - num_1)

    if temp_result_1 <= temp_result_2:
        return num_1
    return num_2


if __name__ == '__main__':
    N = int(input())
    house = list(map(int, input().split()))
    print(main())
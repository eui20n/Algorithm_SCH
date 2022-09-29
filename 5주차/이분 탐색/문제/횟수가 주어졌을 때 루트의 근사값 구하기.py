"""
        횟수가 주어졌을 때, 주어지는 루트값의 근사값 구하기
"""


def binary_search(target_num, error):
    start = - target_num ** 2
    end = target_num ** 2
    cnt = 0

    while True:
        if start >= end:
            return start

        mid = (start + end) / 2  # 몫만 보면 안됨 -> 당연히 그럼 mid 값은 무조건 1임

        cnt += 1

        if mid > target_num:
            end = mid

        elif mid < target_num:
            start = mid

        else:
            return mid

        if cnt == error:
            return mid


if __name__ == "__main__":
    num = 2 ** (1 / 2)  # 사용자가 설정
    range_error = 30  # 사용자가 설정 -> 30번 정도하면 거의 근사하게 나옴
    print(num)
    print(binary_search(num, range_error))


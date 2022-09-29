"""
        루트와 같은 값을 계산할 것임
        수를 정확하게 모르니까 오차의 범위보다는 반복횟수로 생각하는 것이 편할 듯
"""


def binary_search(target_num, error):
    start = - target_num ** 2
    end = target_num ** 2
    cnt = 0

    while True:
        if start >= end:
            return start

        mid = (start + end) / 2 # 몫만 보면 안됨 -> 당연히 그럼 mid 값은 무조건 1임

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
    num = 2 ** (1/2) # 사용자가 설정
    range_error = 30 # 사용자가 설정
    print(num)
    print(binary_search(num, range_error))



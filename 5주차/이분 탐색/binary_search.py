"""
        초기에 시작점과 끝점이 있음
        그 점에서 부터 탐색 범위를 계속 줄이면서 원하는 값을 찾는 방법
"""


def binary_search(array, target, start, end):
    while True:
        if start >= end:
            break

        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1


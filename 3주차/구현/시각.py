def clock():
    """ 시각 함수 """
    N = int(input())

    result = 0

    for hour in range(0, N + 1):
        for minute in range(60):
            for second in range(60):
                if "3" in str(hour):
                    result += 1
                    continue

                if "3" in str(minute):
                    result += 1
                    continue

                if "3" in str(second):
                    result += 1

    print(result)


if __name__ == "__main__":
    clock()

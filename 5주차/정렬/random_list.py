import random


def make_random_list(N):
    random_list = set()

    while True:
        if len(random_list) == N:
            break

        temp_num = random.randint(0, N * 10)
        if temp_num in random_list:
            continue

        random_list.add(temp_num)

    return list(random_list)
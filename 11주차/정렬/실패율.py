def solution(N, stages):
    answer = [[0, x] for x in range(1, N + 1)]

    person = len(stages)

    for idx in range(len(stages)):
        stage = stages[idx]

        if stage > N:
            continue

        answer[stage - 1][0] += 1

    for idx in range(N):
        temp_person = answer[idx][0]
        answer[idx][0] = temp_person / person
        person -= temp_person

    answer.sort(key=lambda x: (-x[0], x[1]))

    for fail, idx in answer:
        print(idx, end=" ")


if __name__ == "__main__":
    N = 4
    stages = [4, 4, 4, 4, 4]
    solution(N, stages)

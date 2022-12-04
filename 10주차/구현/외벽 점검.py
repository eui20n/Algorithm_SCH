from itertools import permutations


def solution(n, weak, dist):
    weak_length = len(weak)

    for i in range(weak_length):
        weak.append(weak[i] + n)

    answer = float('inf')

    for start in range(weak_length):
        for friend in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friend[cnt - 1]

            for i in range(start, start + weak_length):
                if position < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[i] + friend[cnt - 1]

            answer = min(cnt, answer)

    if answer > len(dist):
        return -1
    return answer


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))